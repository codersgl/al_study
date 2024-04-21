from collections import deque


# # 顺序队列
# class Squeue:
#     # 初始化一个空队列
#     def __init__(self):
#         self.elem = []
#         self.front, self.rear = 0, 0
#
#     def __len__(self):
#         return self.rear - self.front
#
#     def enqueue(self, e):
#         self.elem.append(e)
#         self.rear += 1
#
#     def dequeue(self):
#         if self.front == self.rear:
#             raise Exception("队列已空")
#         e = self.elem[self.front]
#         self.front += 1  # 头指针后移代表删除头元素
#         return e
#
#     def get_head(self):
#         if self.front == self.rear:
#             raise Exception("队列已空")
#         return self.elem[self.front]
#
#     def show(self):
#         if self.front == self.rear:
#             raise Exception("队列已空")
#         else:
#             i = 0
#             while i < len(self.elem):
#                 print(self.elem[i], end=" ")
#                 i += 1


# 双向链表
class LNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class Linklist:
    def __init__(self):
        self.head = LNode(None)
        self.tail = LNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node, new_node, after=True):
        """
        插入新节点new_node，如果after为True，则在node之后插入，否则在node之前插入
        """
        if after:
            new_node.prev = node
            new_node.next = node.next
            node.next = new_node
            new_node.next.prev = new_node
        else:
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node

    def remove(self, val):
        """
        移除具有指定值val的节点
        """
        node = self.head
        while node is not None:
            if node.data == val:
                if node.next is not None:
                    node.next.prev = node.prev
                if node.prev is not None:
                    node.prev.next = node.next
                return
            node = node.next

    def locate_elem(self, e):
        """
        找到具有指定值e的节点，如果不存在则返回None
        """
        node = self.head
        while node is not None:
            if node.data == e:
                return node
            node = node.next
        return None

    def __str__(self):
        output = ""
        node = self.head.next
        while node != self.tail:
            output += str(node.data) + ' '
            node = node.next
        return output


def queue_arrangement(N):
    queue = deque([1])
    for i in range(2, N + 1):
        k, p = map(int, input().split())
        if p == 0:
            queue.insert(queue.index(k), i)
        else:
            queue.insert(queue.index(k) + 1, i)
    m = int(input())
    for _ in range(m):
        x = int(input())
        try:
            queue.remove(x)
        except ValueError:
            pass
    return queue


if __name__ == '__main__':
    """法一"""
    # input
    n = int(input())
    # process
    # 好像这道题和队列没啥关系， 哈哈~
    # squeue = Squeue()
    lis = [1]
    for i in range(2, n + 1):
        k, p = map(int, input().split())
        if p == 0:
            lis.insert(lis.index(k), i)
        else:
            lis.insert(lis.index(k) + 1, i)
    m = int(input())
    for j in range(m):
        x = int(input())
        try:
            lis.remove(x)
        except ValueError:
            pass
    print(*lis)

    """法二"""

    n = int(input())
    lq = Linklist()
    lq.insert(lq.head, LNode(1), after=True)
    for i in range(2, n + 1):
        k, p = map(int, input().split())
        node = lq.locate_elem(k)
        lq.insert(node, LNode(i), after=p == 1)
    m = int(input())
    for _ in range(m):
        x = int(input())
        try:
            lq.remove(x)
        except ValueError:
            pass
    print(lq)

    """法三"""
    # 调用函数
    result = queue_arrangement(n)
    print(*result)
