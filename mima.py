#// 将 s[j] 向上拨动一次
def plusOne( s:str, j:int) ->str :
    ch = [ i for i in s ]
    if ch[j] == '9':
        ch[j] = '0'
    else:
        ch[j] =  str(int(ch[j]) + 1)
    return "".join(ch)

#// 将 s[i] 向下拨动一次
def minusOne(s:str, j:int) ->str :
    ch = [i for i in s]
    if  ch[j] == '0':
        ch[j] = '9'
    else:
        ch[j] =  str(int(ch[j])- 1)
    return "".join(ch)


class trr:
  def __init__(self, p ,d):
      self.p = p
      self.d = d


def BFS(deadends:[str], target : str):
   q = []
   q.append("0000")
   vs = set("0000")
   dds = set(deadends)
   step = 0
   rt = trr(None,"0000")
   p = rt
   while len(q)>0:
       lq = len(q)
       #将当前队列种的所有节点向四周扩散
       for i in range(lq):
           cur = q.pop()

           trr(p,cur)


           if dds.__contains__(cur):
               continue

           if cur == target:
               return step, vs
           #将一个节点的相邻节点加入队列
           for j in range(4):

               t= plusOne(cur, j)
               if not vs.__contains__(t):
                    vs.add(t)
                    q.append(t)
               t= minusOne(cur,j)
               if not vs.__contains__(t):
                    vs.add(t)
                    q.append(t)
       step+=1


if __name__ == '__main__':
    print(BFS(["0201","0101","0102","1212","2002"],"0202"))

    for i in range(10):
        print(i)