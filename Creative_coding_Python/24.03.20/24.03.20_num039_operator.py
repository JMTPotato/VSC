#operator 모듈  example = operator.add(10,20) = 30
#    + = add()
#    - = sub()
#    * = mul()
#    / = truediv()
#    % = mod()
#    // = floordiv()
#    ** = pow()

#    == = eq()  equal
#    != = ne()  not equal
#    >  = gt()  greater
#    >= = ge()  greater or equal
#    <  = lt()  little
#    <= = le()  lilttle or equal

#    and = and_()   and_(True, False)
#    or   = or_()   or_(True, False)
#    not = not_()   not_(True)

import operator

num1 = 10
num2 = 3

operator.eq(num1, num2) #False  num1 == num2
operator.ne(num1, num2) #True   num1 != num2
operator.gt(num1, num2) #True   num1 > num2
operator.ge(num1, num2) #True   num1 >= num2
operator.lt(num1, num2) #False  num1 < num2
operator.le(num1, num2) #False  num1 <= num2

flag1 = True
flag2 = False
operator.and_(flag1, flag2) #False  flag1 and flag2
operator.or_(flag1, flag2)  #True   flag1 or flag2
operator.not_(flag1)        #False  not flag1