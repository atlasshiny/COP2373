from pathlib import Path
import csv
import numpy as np


def load_grades(csv_path):
    """Read CSV at ``csv_path`` and return a tuple ``(grades_array, exam_headers)``.

    Returns:
    - grades_array: NumPy array with shape (n_students, n_exams)
    - exam_headers: list of exam column names (e.g. ['Exam 1', 'Exam 2', ...])
    """
    csv_path = Path(csv_path)
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # read header row
        rows = [row for row in reader if row]

    # Extract exam column names (everything after the first two name columns)
    exam_headers = header[2:]

    # Parse numeric exam values into a list of lists
    grades = []
    for row in rows:
        # Skip incomplete rows
        if len(row) < 2 + len(exam_headers):
            continue
        # Convert each exam entry to float
        exam_values = [float(x) for x in row[2:2 + len(exam_headers)]]
        grades.append(exam_values)

    # Convert to NumPy array for vectorized stats
    grades_array = np.array(grades, dtype=float)
    return grades_array, exam_headers

def exam_statistics(grades):
    """Compute per-column statistics for a 2D NumPy array.

    Parameters:
    - grades: NumPy array shaped (n_students, n_exams)

    Returns: dict with keys 'mean','median','std','min','max'
    """
    return {
        'mean': np.mean(grades, axis=0),
        'median': np.median(grades, axis=0),
        'std': np.std(grades, axis=0, ddof=0),
        'min': np.min(grades, axis=0),
        'max': np.max(grades, axis=0),
    }

def overall_statistics(grades):
    """Compute statistics across all exam values (flattened).

    Returns dict with scalar values for mean, median, std, min, max.
    """
    flat = grades.ravel()
    return {
        'mean': float(np.mean(flat)),
        'median': float(np.median(flat)),
        'std': float(np.std(flat, ddof=0)),
        'min': float(np.min(flat)),
        'max': float(np.max(flat)),
    }

def pass_fail_counts(grades, passing=60.0):
    """Determine pass/fail counts per exam and overall pass percentage.

    Parameters:
    - grades: NumPy array shaped (n_students, n_exams)
    - passing: numeric threshold (inclusive) to consider a passing grade

    Returns: (pass_counts, fail_counts, overall_pass_percentage)
    - pass_counts, fail_counts: 1D integer arrays of length n_exams
    - overall_pass_percentage: float in [0.0, 100.0]
    """
    passed_mask = grades >= passing
    pass_counts = np.sum(passed_mask, axis=0).astype(int)
    fail_counts = (grades.shape[0] - pass_counts).astype(int)
    overall_pass_pct = float(np.sum(passed_mask) / passed_mask.size * 100.0)
    return pass_counts, fail_counts, overall_pass_pct

def format_and_print(grades, exam_headers, per_stats, pass_counts, fail_counts, overall_stats, overall_pass_pct, show_rows=5):
    """Print a human-readable summary of the computed statistics.

    - show_rows controls how many student rows to display from the top.
    """
    # Print the first few rows to inspect data shape and values
    print("First few rows (students x exams):")
    # Show at most show_rows rows
    n_show = min(show_rows, grades.shape[0])
    print(grades[:n_show])
    print()

    # Per-exam statistics
    for idx, col in enumerate(exam_headers):
        print(f"{col}:")
        print(f"Mean : {per_stats['mean'][idx]:.2f}")
        print(f"Median : {per_stats['median'][idx]:.2f}")
        print(f"Std : {per_stats['std'][idx]:.2f}")
        print(f"Min : {int(per_stats['min'][idx])}")
        print(f"Max : {int(per_stats['max'][idx])}")
        print(f"Passed : {int(pass_counts[idx])}")
        print(f"Failed : {int(fail_counts[idx])}")
        print()

    # Overall statistics across all exams
    print("Overall (all exams combined):")
    print(f"Mean : {overall_stats['mean']:.2f}")
    print(f"Median : {overall_stats['median']:.2f}")
    print(f"Std : {overall_stats['std']:.2f}")
    print(f"Min : {int(overall_stats['min'])}")
    print(f"Max : {int(overall_stats['max'])}")
    print(f"Overall pass percentage across all exams: {overall_pass_pct:.2f}%")

def main(csv_filename='grades.csv', passing_threshold=60.0):
    """Main entry point: load data, compute stats and print results.

    Parameters are given defaults so the function can be imported and called programmatically.
    """
    csv_file = Path(__file__).parent / csv_filename

    # Load grades and exam headers from the CSV file
    grades, exam_headers = load_grades(csv_file)

    # Compute per-exam and overall statistics
    per_stats = exam_statistics(grades)
    overall_stats = overall_statistics(grades)

    # Compute pass/fail counts and overall pass percentage
    pass_counts, fail_counts, overall_pass_pct = pass_fail_counts(grades, passing=passing_threshold)

    # Print formatted results
    format_and_print(grades, exam_headers, per_stats, pass_counts, fail_counts, overall_stats, overall_pass_pct)

if __name__ == '__main__':
    main()
