module Player (
    playCard,
    makeBid
)
where
{-
1. Assuming the game starts with cards already dealt to us (the player) once ran, we 
first determine the bid. 

2. Bids made are based on the number of cards in hand with the same suit as the trump 
card (trump cards). Strategy is applied with the number of trump cards as default bid 
because the probability to win a round based on suit is at least the number of trump 
cards. 

3. Bid as it is if we are not the last player. However, we are to obey hook rule if 
we are the last player. 

4. If we somehow do not satisfy the hook rule, reduce our bid by one or increment our 
bid by one (applied when our original bid is 0 which indicates lack of trump cards). 
Strategy is applied with reducing bid as the default decision as chances are low for 
the last player to win with the consideration of card ranking build up by previous 
players. 

5. Play starts after every player announce their bid. 

6. We play out the lowest ranked card if we are the leading player. Strategy is 
applied so because chances are low for the leading player to win with the 
consideration of card ranking build up by later players after observing our card. 

7. If we are not the leading player and our bid is 0, we play out the lowest ranked 
card out of cards in hand with the same suit as the leading suit (leading suit cards). 
If we happen to not have any leading suit cards, we play out the lowest ranked trump 
card or otherwise, the lowest ranked of any card. Strategy is applied so to reduce the 
chances of winning. 

8. If we are not the leading player and we have won as many tricks as our bid, we 
play out the lowest ranked leading suit card. If we happen to not have any leading 
suit cards, we play out the lowest ranked trump card or otherwise, the lowest ranked 
of any card. Strategy is applied so to reduce the chances of winning further. 

9. If we are not the leading player and we have won more/less tricks than our bid, we 
play out the highest ranked leading suit card. If we happen to not have any leading 
suit cards, we play out the highest ranked trump card or otherwise, the highest ranked 
of any card. Strategy is applied so to increase the chances of winning to reach our bid 
quota or to earn as many points as possible since the 10 points are forfeited due to 
exceeding our bid quota.  
-}

import OhTypes
import OhHell

{-|
    The 'result' function returns the number of times the player won
    It takes 3 arguments namely:
        idPlayer (type PlayerId): the player's id
        trumpSuit (type Suit): the suit of the trump card
        roundsPlayed (type [Trick]): a list of list of tuples 
        (type (Card Suit Rank, PlayerId)); list of list of cards played by each 
        player in each round/trick
-}
result:: PlayerId -> Suit -> [Trick] -> Int
result _ _ [] = 0 -- ^condition when no winnings
result idPlayer trumpSuit roundsPlayed = length $ filter (==idPlayer) $ (winner trumpSuit <$> roundsPlayed)

{-|
    The 'placeCard' function returns the card to play out after choosing the 
    group of cards; either trump cards, leading cards or cards in hand
    It takes 3 arguments namely:
        f (type ([a] -> a)): a function to determine which card to return out of 
        the list of cards passed
        cardList (type [[a]]): a list of list of cards grouped by type of suit
        hand (type [a]): the list of cards in hand
-}
placeCard::([a] -> a) -> [[a]] -> [a] -> a
placeCard f cardList hand | (sum $ length <$> cardList) == 0 = f hand -- ^condition when lack of trump cards and leading suit cards
placeCard f cardList _ = f $ head $ filter ((0/=) . length) cardList

{-|
    The 'getHighest' function returns the highest ranked card
    It takes 1 argument namely:
        []/[c]/(h@(Card _ r)):s@(Card _ rr):cs) (type [Card]): a list of  
        cards which exist in hand
-}
getHighest::[Card] -> Card
getHighest [] = error "No cards in hand"
getHighest [c] = c
getHighest (h@(Card _ r): s@(Card _ rr): cs)
    | r < rr = getHighest (s:cs)
    | otherwise = getHighest (h:cs)

{-|
    The 'getLowest' function returns the lowest ranked card
    It takes 1 argument namely:
        []/[c]/(h@(Card _ r)):s@(Card _ rr):cs) (type [Card]): a list of  
        cards which exist in hand
-}
getLowest::[Card] -> Card
getLowest [] = error "No cards in hand"
getLowest [c] = c
getLowest (h@(Card _ r): s@(Card _ rr): cs)
    | r < rr = getLowest (h:cs)
    | otherwise = getLowest (s:cs)

{-|
    The 'lift' function returns function applied a and b parameters
    It takes 3 arguments namely:
        f (type (a -> -> c)): a function which is a type constructor of the 
        applicative typeclass
        a and b: parameters to apply the function on
-}    
lift::Applicative f => (a -> b -> c) -> f a -> f b -> f c
lift f a b = f <$> a <*> b

{-|
    The 'getBid' function returns the player's bid
    It takes 2 arguments namely:
        idPlayer (type String): the player's id  
        list (type [(PlayerId, Int)]): a list of tuples of bids placed by each 
        player
-}
getBid::String -> [(PlayerId, Int)] -> Int
getBid _ [] = error "No bids placed" 
-- getBid idPlayer list | filter ((idPlayer==) . fst) list == [] = 0
getBid idPlayer list = snd $ head $ filter ((idPlayer==) . fst) list

{-|
    The 'getSuit' function returns the card suit
    It takes 1 argument namely:
        (Card suit _) (type Card): the card
-}
getSuit::Card -> Suit
getSuit (Card suit _) = suit

{-|
    The 'getHighest' function returns the list of cards in hand with the same 
    suit as the the suit passed in
    It takes 2 arguments namely:
        suit (type Suit): a card's suit
        hand (type [Card]): the list of cards in hand
-}
getCardsOfSuit::Suit -> [Card] -> [Card]
getCardsOfSuit suit hand = filter ((suit==) . getSuit) hand

{-|
    The 'playCard' function returns the card to play out after evaluating game 
    condition
    The function is of type PlayFunc which parameters' type has been defined in 
    OhTypes.hs
    It takes 6 arguments namely:
        idPlayer: the player's id
        cards: the list of cards in hand
        bidTuples: a list of tuples of bids placed by each player
        trump: the trump card
        playedCards: a list of list of tuples 
        (type (Card Suit Rank, PlayerId)); list of list of cards played by each 
        player in each round/trick
        cardsOut: list of cards on the table
-}
-- | Play a card for the current trick.
-- If you are the "lead" player, you must follow the suit of the card that was led.
playCard :: PlayFunc
playCard idPlayer cards bidTuples trump playedCards cardsOut
    | True `elem` firstCond = -- ^condition to check if player is the leading player or player bids 0 and not (player is leading player && player bids 0)
        case head firstCond of
            True -> getLowest cards -- ^condition for leading player
            False -> placeCard getLowest list cards -- ^condition when bid is 0
    | head $ secondCond = placeCard getLowest list cards -- ^condition when winnings equals to bid
    | otherwise = placeCard getHighest list cards -- ^condition when winnings are more/less than bid
    where
        leadingSuit = getSuit $ fst $ last cardsOut
        trumpSuit = getSuit $ trump
        trumpCards = getCardsOfSuit trumpSuit cards
        leadingSuitCards = getCardsOfSuit leadingSuit cards
        list = [leadingSuitCards, trumpCards]
        firstCond = lift (==) [0] [(length cardsOut), (getBid idPlayer bidTuples)]
        secondCond = lift (==) [result idPlayer trumpSuit playedCards] [getBid idPlayer bidTuples]

{-|
    The 'makeBid' function returns the player's bid before the play starts
    The function is of type BidFunc which parameters' type has been defined in 
    OhTypes.hs
    It takes 4 arguments namely:
        trump: the trump card
        cards: the list of cards in hand
        players: number of player in the game
        bidTuples: the list of bids placed
-}
-- | Bid the number of cards you can win based on the trump card and your hand.
--   last player to bid must obey "hook rule":
--   sum of bids must not equal number of tricks available
makeBid :: BidFunc
makeBid trump cards players bidList
    | length bidList < players - 1 = n -- ^condition for leading player & otherwise
    | hookRule bids players (length cards) = n -- ^condition for last player
    | head $ cond = n+1 -- ^condition for last player when default bid is 0 to prevent negative bidding
    | otherwise = n-1 -- ^condition for last player && when default bid is more than 0
    where 
        bids = bidList ++ [n]
        n = length $ getCardsOfSuit (getSuit trump) cards
        cond = lift (==) [0] [n]