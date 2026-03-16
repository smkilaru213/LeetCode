class Solution {
    public String mergeAlternately(String word1, String word2) {
        String ret = "";
        String shorter = "";
        String longer = "";
        if (word1.length() > word2.length()) {
            shorter = word2;
            longer = word1;
        } else {
            shorter = word1;
            longer = word2;
        }

        for (int i = 0; i < shorter.length(); i++) {
            ret += word1.charAt(i);
            ret += word2.charAt(i);
        }

        ret += longer.substring(shorter.length());
        return ret;
    }
}