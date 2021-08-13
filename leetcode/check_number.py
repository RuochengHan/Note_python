class Solution:

    def check1(self, s: str):
        if s == '':
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        s_split = s.split('.')

        if len(s_split) == 1:
            b1 = self.check2(s_split[0], necessary=True)
            return b1

        elif len(s_split) == 2:
            s1,s2 = s_split
            if s1 == '' and s2 == '':
                return False

            b1 = self.check2(s1, necessary=False)
            b2 = self.check2(s2)
            return b1 and b2

        else:
            return False

    def check2(self, s: str, necessary=False, exp=False):

        if s == '':
            if necessary:
                return False
            else:
                return True

        if exp and (s[0] == '+' or s[0] == '-'):
            
            s = s[1:]     
            if s == '':
                return False

        for i in s:
            if i not in self.x:
                return False
        
        return True

    def isNumber(self, s: str) -> bool:

        self.x = [str(i) for i in range(10)]
        s = s.strip()

        if s == '':
            return False

        s_split = s.replace('E','e').split('e')
        if len(s_split) == 1:
            b1 = self.check1(s_split[0])
            return b1

        elif len(s_split) == 2:
            s1,s2 = s_split
            if s1 == '' and s2 == '':
                return False

            b1 = self.check1(s1)
            b2 = self.check2(s2, necessary=True, exp=True)
            return b1 and b2

        else:
            return False
