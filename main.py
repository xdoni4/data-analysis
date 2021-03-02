
def leven_length(word1, word2):
    table = []
    for i in range(len(word1)+1):
        table.append([])
        for j in range(len(word2)+1):
            table[i].append(0)
    for i in range(1, len(word1)+1):
        table[i][0] = i
    for j in range(1, len(word2)+1):
        table[0][j] = j
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            var = 0
            if word1[i-1] != word2[j-1]:
                var = 1
            table[i][j] = min(min(table[i][j-1]+1, table[i-1][j]+1), table[i-1][j-1]+var)
    return table[len(word1)][len(word2)]


words = []
k = int(input())
border = int(input())
kk = k
while k:
    word = input()
    words.append(word)
    k -= 1

clusters = {}
active = []
for i in range(len(words)):
    clusters[i] = {i}
    active.append(1)

dp = []
for i in range(len(words)):
    dp.append([])
    for j in range(len(words)):
        dp[i].append(-1)

for i in range(len(words)):
    for j in range(len(words)):
        dp[i][j] = leven_length(words[i], words[j])
for q in range(10):
    lens = []
    for keyi, vali in clusters.items():
        for keyj, valj in clusters.items():
           if active[keyi] and active[keyj] and keyi != keyj:
               lens.append((dp[keyi][keyj], (keyi, keyj)))
    used = []
    for i in range(kk):
        used.append(0)
    lens.sort()
    for pair in lens:
        first = pair[1][0]
        second = pair[1][1]
        if not used[first] and not used[second] and not first == second and pair[0] <= border:
            used[first] = 1
            used[second] = 1
            clusters[first] = set.union(clusters[first], clusters[second])
            clusters.pop(second, None)
            for i in range(len(clusters)):
                if not i == first and not i == second:
                    dp[i][first] = (dp[i][first] + dp[i][second])/2
                    dp[first][i] = dp[i][first]
print(clusters)