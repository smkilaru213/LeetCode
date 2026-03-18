class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int initMostCandies = 0;
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] >= initMostCandies) {
                initMostCandies = candies[i];
            }
        }

        List<Boolean> result = new ArrayList<>();
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= initMostCandies) {
                result.add(true);
            } else {
                result.add(false);
            }
        }

        return result;
    }
}