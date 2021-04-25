import torch

x = torch.rand([5,3])
y = torch.rand([5,3])
print('x:',x)
print('y:',y)
print('x+y:',x+y)
print('x+y:',torch.add(x,y))


# inplace=True代表不创建新的对象，而是在旧的对象上进行修改
# 其中pytorch的inplace版本的操作名字有末尾_，如x.copy_(y)
x.copy_(y)
print('new_x:',x)

# 索引