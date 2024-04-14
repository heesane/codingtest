class Solution {
    public long[] solution(int x, int n) {
        long[] l = new long[n];
        for(int i = 0;i<n;i++){
            l[i] = (long)x + (long)x * i;
        }
        return l;
    }
}