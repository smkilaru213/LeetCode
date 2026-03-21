class Solution {
    public String reverseWords(String s) {
        String[] words = s.strip().split(" ");
        String ret = "";

        for (int i = words.length - 1; i >= 0; i--) {
            String str = words[i].strip();
            if (str == "") {
                continue;
            }
            if (i == 0) {
                ret += str;
            } else {
                ret += str;
                ret += " ";
            }
        }
        return ret;
    }
}