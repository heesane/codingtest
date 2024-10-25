class Solution {
    public boolean solution(int x) {
        if(x % Integer.toString(x).chars().map(Character::getNumericValue).sum() == 0){
            return true;
        }else return false;
        
    }
}