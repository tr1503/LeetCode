public int findMaxScore(int[] cards) {
    int[] memo = new int[cards.length];
    int sum = 0;
    for (int card: cards) sum += card;
    return (sum + helper(cards, 0, memo)) / 2;
}
 
public int helper(int[] cards, int cur, int[] memo) {
    if (cur == cards.length - 1) return cards[cur];
    if (cur == cards.length - 2) return Math.max(cards[cur] - cards[cur + 1], cards[cur] + cards[cur + 1]);
    if (cur == cards.length - 3) {
        int valOne = cards[cur] - Math.max(cards[cur + 1] - cards[cur + 2], cards[cur + 1] + cards[cur + 2]);
        int valTwo = cards[cur] + cards[cur + 1] - cards[cur + 2];
        int valThree = cards[cur] + cards[cur + 1] + cards[cur + 2];
        return Math.max(valOne, Math.max(valTwo, valThree));
    }
    if (memo[cur] > 0) return memo[cur];
    int oneCardValue = cards[cur] - helper(cards, cur + 1, memo);
    int twoCardValue = cards[cur] + cards[cur + 1] - helper(cards, cur + 2, memo);
    int threeCardValue = cards[cur] + cards[cur + 1] + cards[cur + 2] - helper(cards, cur + 3, memo);
    memo[cur] = Math.max(oneCardValue, Math.max(twoCardValue, threeCardValue));
    return memo[cur];
}
