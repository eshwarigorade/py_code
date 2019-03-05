num = 100
print(num)
print(class(num))

num1 = 10L
print("num1", num1)
print(class(num1))

name = "ABCD"
print(name)
print(class(name))

number = c(1, 2, 3, 4)
print(number)

numbers = 1:10
print(numbers)
print(numbers[1])
print(numbers[1:3])
print(numbers[c(-1,-2)])

for (number in numbers){
  print(number)
}
number1=c(10,20,30,40)
names=c('wer','qwe','tyu')
l1=list(c(number1,names))
print(class(l1))
print(l1[1])
print(l1[[1]])
print(l1[[1]][2])
print(l1$number1)
l2=list(age=c(20,21),course=c('p1','p2','p3'))
print(l2$age)
print(l2$age[2])
v1=c(1,2,3,4,5)
v2=c(6,7,8,9,10)
print(v1+v2)
print(v1-v2)
print(v1 & v2)
print(v1 && v2)
print(v1 | v2)
print(v1 || v2)
v3=c(1,2,3,4)
v4=c(1,2,3,5)
print(v3+v4)
complex1= 2+3i
complex2= 4+2i
print(complex1+complex2)
v6=c(1+2i,3+3i,4+4i)
v7=c(5+5i,6+6i,7+7i)
print(v6+v7)