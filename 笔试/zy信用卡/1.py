def new21Game(N, K, W):
        dp = [0.0]*(N+W+2)
        sum = [0.0]*(N+W+2)
        for i in range(N+W+1,-1,-1):
            if i>N: continue
            if i>=K: dp[i]=1.0
            else: dp[i]=(sum[i+1]-sum[i+1+W])/W
            
            sum[i] = sum[i+1]+dp[i]
        
        return dp[0]
N,K,W = map(int,input().split())
print(round(new21Game(N,K,W),5))