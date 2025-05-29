mod = 998244353; base = [[1,1],[1,0]]
def modinv(a): return pow(a,-1,mod)
def mul(A,B):
    ans = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            eij = 0
            for k in range(2): eij += A[i][k]*B[k][j]
            ans[i][j] = eij % mod
    return ans
def mat_pow(b):
    if b == 0: return [[1,0],[0,1]]
    if b == 1: return base
    X = mat_pow(b//2); X = mul(X,X)
    if b%2 == 1: return mul(X,base)
    else: return X
def fib(b): return mat_pow(b)[1][0]
def inv(mat,sz):
    ans = [[+(sz==j-i) if j >= sz else mat[i][j] for j in range(2*sz)] for i in range(sz)]
    for k in range(sz):
        i = k
        while i < sz and ans[i][k] == 0: i += 1
        if i == sz: print(k); raise MemoryError
        for j in range(2*sz): ans[k][j],ans[i][j] = ans[i][j],ans[k][j]
        pivot = modinv(ans[k][k])
        for j in range(2*sz): ans[k][j] = (ans[k][j]*pivot)%mod
        for i in range(sz):
            if i == k: continue
            if ans[i][k] != 0:
                t = ans[i][k]
                for j in range(2*sz):
                    ans[i][j] = (ans[i][j]-t*ans[k][j]) % mod
    return [[ans[i][j+sz] for j in range(sz)] for i in range(sz)]
# F[i][j] = sum of prod Fib(ak) where a1+...+ai=j
F = [[+(i==j) for j in range(202)] for i in range(101)]
for i in range(1,101):
    for j in range(i+1,202):
        F[i][j] = (F[i][j-1] + F[i][j-2] + F[i-1][j-1]) % mod
def solve(N,n):
    '''F[N][n]'''
    if n < N: return 0
    if N == 1: return fib(n)
    if n < 202: return F[N][n]
    mat = [[F[1][i+1] if j < N else F[1][i] for j in range(2*N)] for i in range(2*N)]
    for i in range(2*N):
        for j in range(2*N):
            mat[i][j] *= pow(i+1,j%N,mod)
            mat[i][j] %= mod
    vec,coeff,imat = [F[N][i+1] for i in range(2*N)],[],inv(mat,2*N)
    for i in range(2*N):
        _ = 0
        for j in range(2*N):
            _ = (_ + imat[i][j]*vec[j])%mod
        coeff.append(_)
    Fn,Fnm1,answer = fib(n),fib(n-1),0
    for i in range(N):
        answer += coeff[i] * pow(n,i,mod) * Fn
        answer %= mod
    for i in range(N):
        answer += coeff[i+N] * pow(n,i,mod) * Fnm1
        answer %= mod
    return answer
N,n = map(int,input().split())
print(solve(N,n))