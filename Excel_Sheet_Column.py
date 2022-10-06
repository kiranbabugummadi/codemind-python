alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def num_num(num):
    if num<26:
        return alpha[num-1]
    else:
        q, r=num//26, num%26
        if r==0:
            if q==1:
                return alpha[r-1]
            else:
                return num_num(q-1)+alpha[r-1]
        else:
            return num_num(q)+alpha[r-1]
a=int(input())
print(num_num(a))