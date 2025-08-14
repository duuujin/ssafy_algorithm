# 0813 복습
- 동적 메모리 관리방법 
    - 스택 : 선입후출, 후입선출 - 선형구조
    - 큐 : 선입선출 (front 포인터 , rear 포인터)
---
# 연결 리스트 (Linked List)
- 자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고, 개별적으로 위치하고 있는 각 원소를 연결하여 하나의 전체적인 자료구조를 이룬다
- 링크를 통해 원소에 접근하므로, 리스트에서처럼 물리적인 순서를 맞추기 위한 작업이 필요하지 않다
- 자료구조의 크기를 동적으로 조정할 수 있어, 메모리의 효율적인 사용이 가능하다

# 연결 리스트의 기본 구조
- 노드
    - 연결 리스트에서 하나의 원소를 표현하는 기본 구성 요소
    - 구성요소
        - 데이터 필드
            - 원소의 값을 저장
            - 저장할 원소의 종류나 크기에 따라 구조를 정의하여 사용함
        - 링크 필드
            - 다음 노드의 참조 값을 저장
- 헤드
    - 연결 리스트의 첫 노드에 대한 참조 값을 갖고 있음
---
# 단순 연결 리스트(Singly Linked List)
- 노드가 하나의 링키ㅡ 필드에 의해 다음 노드와 연결되는 구조를 가진다
- 헤드가 가장 앞의 노드를 가리키고, 링크 필드가 연속적으로 다음 노드를 가리킨다
- 링크 필드가 Null인 노드가 연결 리스트의 가장 마지막 노드이다

# 단순 연결리스트 구조체 정의
- 노드와 링크 그리고 헤드를 초기화
```python
class Node:
    def __init__(self,data)
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
```

# 단순 연결리스트 구현 - insert
```python
class SinglyLinkedList:
    ...

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    print("범위를 벗어난 삽입입니다. ")
                    return
                current = current.next
            new_node.next = current.next
            current.next = new.node
```

# 단순 연결리스트 구현 - append
- 리스트의 끝에 노드를 추가하는 메소드
- 끝에 추가하는 작업은 자주 일어나므로 기능을 분리해서 따로 구현
```python
class SinglyLinkedList:
    ...
    def is_empty(self):
        return self.head is None

    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
```

# 단순 연결리스트 구현 - delete
- 특정 위치의 노드를 삭제하는 메소드
```python
class SinglyLinkedList:
    ...
    def delete(self,position):
        if self.is_empty():
            print("싱글 링크드 리스트가 비었습니다.")
            return
        
        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None or current.next is None:
                    print("범위를 벗어났습니다.")
                    return
                current = current.next
            deleted_node = current.next
            deleted_data = deleted_node.data
            current.next = current.next.next
        return deleted_data
```

# 단순 연결리스트 구현 - Search
```python
def search(self, data):
    current = self.head
    position = 0
    while current:
        if current.data = data:
            return position
        current = current.next
        position += 1
    return -1
```

# 단순 연결리스트 구현 - IsEmpty
```python
def is_empty(self):
    return self.head is None
```

# 단순 연결리스트의 장점과 단점
- 장점
    - 필요한 만큼만 메모리 사용
    - 연속된 메모리 블록이 필요하지 않아, 메모리 관리가 더 유연
- 단점
    - 특정 요소에 접근하려면 순차적으로 탐색해야함 -> 시간복잡도: O(N)
    - 역방향 탐색 불가
    - 마지막 요소로 접근하거나 추가하려면 전체 리스트를 순회해야함
    
---

# 이중 연결리스트(Doubly Linked List)
- 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
- 두 개의 링크 필드와 한 개의 데이터 필드로 구성