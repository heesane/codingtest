class Solution {
    public String solution(String phone_number) {
        int answer = phone_number.length() - 4;
        String last = phone_number.substring(phone_number.length() - 4, phone_number.length());
        return "*".repeat(answer) + last;
    }
}