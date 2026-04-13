import random

def main():

    # deck class from textbook + another method
    class Deck():
        def __init__(self, size=52):
            self.card_list = [i for i in range(size)]
            self.cards_in_play_list = []
            self.discards_list = []
            random.shuffle(self.card_list)

        def deal(self):
            if len(self.card_list) < 1:
                random.shuffle(self.discards_list)
                self.card_list = self.discards_list
                self.discards_list = []
                print('Reshuffling...!!!!')
            new_card = self.card_list.pop()
            return new_card

        def new_hand(self):
            self.discards_list += self.cards_in_play_list
            self.cards_in_play_list.clear()
            
        def draw_card(self):
            """Draw a card from the deck without automatically tracking it as in-play.
            Used for replacing cards already in `cards_in_play_list`.
            """
            if len(self.card_list) < 1:
                random.shuffle(self.discards_list)
                self.card_list = self.discards_list
                self.discards_list = []
                print('Reshuffling...!!!!')
            return self.card_list.pop()

    RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    SUITS = ['Clubs','Diamonds','Hearts','Spades']

    def card_to_string(card_int: int) -> str:
        rank = RANKS[card_int % 13]
        suit = SUITS[card_int // 13]
        return f"{rank} of {suit}"


    
    deck = Deck()
    hand = [deck.deal() for _ in range(5)]

    print("Your hand:")
    for i, c in enumerate(hand, start=1):
        print(f"{i}: {card_to_string(c)}")

    user_input = input("Enter positions to replace (e.g. 1,3,5) or press Enter to keep: ")
    if user_input and user_input.strip():
        parts = [p.strip() for p in user_input.split(',') if p.strip().isdigit()]
        # convert to zero-based unique indices within 1..5
        indices = []
        for p in parts:
            n = int(p)
            if 1 <= n <= 5 and (n - 1) not in indices:
                indices.append(n - 1)

        for idx in indices:
            hand[idx] = deck.deal()

    print("\nFinal hand:")
    for i, c in enumerate(hand, start=1):
        print(f"{i}: {card_to_string(c)}")



if __name__ == '__main__':
    main()