```C++
class Solution {
    public:
    int maxSubArray(vector<int>& nums) {
        int sum=0, re=INT_MIN;
        for(int x:nums){
        sum=max(sum+x,x);
        re=max(sum,re);
    }
    return re;
}
```

- sum(i) = Max(<span style="color: red">sum(i -1) + nums[i]</span>,  <span style="color: green">nums[i]</span>)，即如果 sum(i - 1) > 0 则算到 sum(i) 里面，否则 sum(i) 就是 nums[i]
- result = Max(sum[i])
- 可以先在一个循环中求出每个元素 i 的 sum(i)，然后第二个循环中求所有 sum 的 max，也可以在一个循环中完成这两个步骤
