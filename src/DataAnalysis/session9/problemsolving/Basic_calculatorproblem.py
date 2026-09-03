class Solution(object):
    def check_priority(self,op):
         if op=='+'or op=='-':
            return 1
         elif  op=='/'or op=='*':
            return 2
    def is_operator(self,op):
        if op=='+'or op=='/'or op=='*'or op=='-':
            return True
        else :
          return False
    def calc(self,n1,n2,op):
        if op=='+':
            return int(n1)+int(n2)
        elif op=='-':
            return int(n2)-int(n1)
        elif op=='/':
            return int(int(n1) / int(n2))
        elif op=='*':
            return int(n1)*int(n2)
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        oprands=[]
        last_op=""
        oprators=[]
        num = ""
        process=False
        for ind,i in enumerate(s):
            if i==' ':
             continue  
            if self.is_operator(i):

                if process ==True: 
                  res=self.calc(oprands[-1],num,last_op)
                  oprands[-1] = res
                  process=False
                  num = ""
                else :
                    oprands.append(num)       
                    num = ""
                if self.check_priority(i)>1:
                    last_op=i
                    process=True

                else: 
                    oprators.append(i)

                    

            else :
                num += i
        if process: 
                  res=self.calc(oprands[-1],num,last_op)
                  oprands[-1] = res  
        elif num != "":
          oprands.append(num)

        oprators.reverse()
        oprands.reverse()           
        while oprators:
            op = oprators.pop()
            n2 = oprands.pop()
            n1 = oprands.pop()
            res = self.calc(n1, n2, op)
            oprands.append(res)
        return int(oprands[-1])

        