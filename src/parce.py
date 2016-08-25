import re
import calc


class Parser :
    def __init__(self, exp):
        self.expArray = re.findall(r"(?:\d*\.)?\d+|\*|\+|\-|\/|\(|\)", exp)
        self.iter=0

    def parsePrimary(self):
        if (self.iter<self.expArray.__len__())&(self.expArray[self.iter]=="-") :
            self.iter+=1
            return calc.Negate(self.parsePrimary())
        elif (self.iter<self.expArray.__len__())&(self.expArray[self.iter]=="(") :
            self.iter +=1
            res = self.parseExpression()
            self.iter += 1
            return res
        elif (self.iter<self.expArray.__len__())&(bool(re.fullmatch(r"(?:\d*\.)?\d+", self.expArray[self.iter]))) :
            res=self.expArray[self.iter]
            self.iter+=1
            return calc.Value(res)

    def parseMonomial(self):
        res=self.parsePrimary()
        if self.iter<self.expArray.__len__() :
            while (self.expArray[self.iter]=="*")|(self.expArray[self.iter]=="/") :
                if self.expArray[self.iter]=="*" :
                    self.iter += 1
                    res=calc.Multiply(res, self.parsePrimary())
                elif self.expArray[self.iter] == "/":
                    self.iter += 1
                    res = calc.Divide(res, self.parsePrimary())
                if self.iter >= self.expArray.__len__(): break
        return res

    def parseExpression(self):
        res=self.parseMonomial()
        if self.iter < self.expArray.__len__() :
            while (self.expArray[self.iter] == "+") | (self.expArray[self.iter] == "-"):
                if self.expArray[self.iter] == "+":
                    self.iter += 1
                    res = calc.Add(res, self.parseMonomial())

                elif self.expArray[self.iter] == "-":
                    self.iter += 1
                    res = calc.Substract(res, self.parseMonomial())
                if self.iter >= self.expArray.__len__(): break
        return res
