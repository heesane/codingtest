class Solution {
    public int[] solution(int[][] arr) {
        return zip(arr,0,0,arr.length);
    }
    
    private int[] zip(int[][]arr, int x, int y, int size){
        if(canZip(arr,x,y,size)){
            if(arr[x][y] == 1){
                return new int[]{0,1};
            }else{
                return new int[]{1,0};
            }
        }
        
        int box = size / 2;
        
        int[] res1 = zip(arr,x,y,box);
        int[] res2 = zip(arr,x+box,y,box);
        int[] res3 = zip(arr,x,y+box,box);
        int[] res4 = zip(arr,x+box,y+box,box);
        
        return new int[]{res1[0]+res2[0]+res3[0]+res4[0],res1[1]+res2[1]+res3[1]+res4[1]};
        
    }
    
    private static boolean canZip(int[][]arr ,int x,int y, int size){
        int start = arr[x][y];
        for(int i = x; i < x + size; i++){
            for(int j = y; j < y + size; j++){
                if(arr[i][j] != start){
                    return false;
                }
            }
        }
        return true;
    }
}