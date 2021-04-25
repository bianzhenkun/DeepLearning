import torch

# x = torch.rand([5,3])
# y = torch.rand([5,3])
# print('x:',x)
# print('y:',y)
# print('x+y:',x+y)
# print('x+y:',torch.add(x,y))


# inplace=True代表不创建新的对象，而是在旧的对象上进行修改
# 其中pytorch的inplace版本的操作名字有末尾_，如x.copy_(y)
# x.copy_(y)
# print('new_x:',x)
# y.add_(x)
# print('y:',y)

# 改变形状
# z = x.view([3,5])
# print(z)
# z = x.clone().view(15)
# z += 1
# print('z:',z)
# print('x:',x)

# 广播机制
x = torch.arange(1, 3).view(1, 2)
print(x)
y = torch.arange(1, 4).view(3, 1)
print(y)
print(x + y)
# 由于x和y分别是1行2列和3行1列的矩阵，如果要计算x + y，
# 那么x中第一行的2个元素被广播（复制）到了第二行和第三行，而y中第一列的3个元素被广播（复制）到了第二列。
# 如此，就可以对2个3行2列的矩阵按元素相加。