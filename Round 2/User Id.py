def Solution(string, i,length, u, ans, r):
    vowels = ['a','e', 'i', 'o', 'u']
    if i>=len(string)-1 and u<r:
        return 0
    elif i>=len(string)-1 and u==r and length>=3:
        return ans+1
    elif i>=len(string)-1:
        return 0
    elif (string[i] not in vowels and string[i+1] not in vowels) and length>=3:
        a1 = Solution(string,i+1,length+1,u,ans,r)
        a2 = Solution(string,i+1,0,u+1,ans,r)
        return a1+ a2
    else:
        return Solution(string, i+1, length+1,u,ans,r)
        


users = int(input())
string = input()

#Solution(string, start_character, length, users_splitted, ans_count, required_users)
answer = Solution(string, 0, 0, 1, 0, users)
print(answer)
