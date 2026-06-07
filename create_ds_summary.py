"""
Data Structures & Algorithms Study Summary
60 items: 40 highlighted from PDFs + 20 additional definitions
"""
import json, re
from datetime import date

# ── Color constants ─────────────────────────────────────────────
KEYWORDS_RED    = {"always","never","must","cannot","only","critical",
                   "important","warning","do not","not","must not","never"}
KEYWORDS_ORANGE = {"note","required","ensure","before","constant","linear",
                   "logarithmic","quadratic"}

def colorize(text):
    parts = re.split(r'(\s+)', text)
    out = []
    for p in parts:
        tok = p.lower().strip(".,;:()")
        if tok in KEYWORDS_RED:
            out.append(f'<span class="kw-red">{p}</span>')
        elif tok in KEYWORDS_ORANGE:
            out.append(f'<span class="kw-orange">{p}</span>')
        else:
            out.append(p)
    return "".join(out)

def term(name, definition, badge=None):
    badge_html = ""
    if badge == "green":
        badge_html = '<span class="badge-green">GREEN</span> '
    elif badge == "yellow":
        badge_html = '<span class="badge-yellow">YELLOW</span> '
    elif badge == "red":
        badge_html = '<span class="badge-red">RED</span> '
    return (f'<p class="term">{badge_html}'
            f'<span class="term-name">{name}:</span> '
            f'{colorize(definition)}</p>')

def code(line):
    return f'<pre class="code">{line}</pre>'

def tip(text):
    return f'<div class="tip"><strong>Exam Tip:</strong> {colorize(text)}</div>'

def trap(text):
    return f'<div class="trap"><strong>Exam Trap:</strong> {colorize(text)}</div>'

def bullet(text):
    return f'<li>{colorize(text)}</li>'

def chapter(title):
    return f'<h2>{title}</h2>'

def section(title):
    return f'<h3>{title}</h3>'

def divider(title):
    return f'<div class="divider">{title}</div>'

# ── CSS ─────────────────────────────────────────────────────────
CSS = """
@page {
    size: A4;
    margin: 16mm 18mm 16mm 18mm;
    @bottom-right {
        content: counter(page);
        font-size: 9pt; color: #888;
    }
}
.cover {
    page-break-after: always;
    text-align: center;
    padding: 50pt 30pt;
    border: 2px solid #1F3964;
    border-radius: 8pt;
    background: linear-gradient(150deg,#EBF3FB,#F8FBFF);
    min-height: 230mm;
    box-sizing: border-box;
}
body {
    font-family: Calibri, Arial, sans-serif;
    font-size: 9.5pt;
    color: #222;
    line-height: 1.45;
}
h1 { color:#1F3964; font-size:24pt; margin:0 0 6pt; }
.subtitle { color:#17738F; font-size:13pt; margin:4pt 0; }
.course   { font-size:11pt; font-weight:bold; margin:6pt 0; }
.date-line{ color:#888; font-size:10pt; }
.legend   { margin: 8pt 0; font-size:9pt; }
h2 {
    color:#1F3964; font-size:12.5pt; font-weight:bold;
    border-bottom: 2px solid #1F3964;
    padding-bottom:2pt; margin:0; margin-bottom:4pt;
    page-break-before: always;
}
h3 {
    color:#17738F; font-size:10pt; font-weight:bold;
    margin-top:8pt; margin-bottom:2pt;
}
.divider {
    background:#1F3964; color:white;
    font-size:11pt; font-weight:bold;
    padding:5pt 10pt; margin:8pt 0;
    border-radius:4pt;
    page-break-before: always;
}
p.term {
    margin: 2.5pt 0 2.5pt 10pt;
    font-size: 9.5pt;
}
span.term-name { color:#0070C0; font-weight:bold; }
span.kw-red    { color:#C00000; font-weight:bold; }
span.kw-orange { color:#C05500; font-weight:bold; }
.badge-green  {
    background:#70AD47; color:white; font-size:7pt; font-weight:bold;
    padding:1pt 4pt; border-radius:3pt; margin-right:4pt;
}
.badge-yellow {
    background:#FFB900; color:#222; font-size:7pt; font-weight:bold;
    padding:1pt 4pt; border-radius:3pt; margin-right:4pt;
}
.badge-red {
    background:#FF4B6E; color:white; font-size:7pt; font-weight:bold;
    padding:1pt 4pt; border-radius:3pt; margin-right:4pt;
}
pre.code {
    font-family:'Courier New',monospace; font-size:8pt;
    background:#F2F2F2; color:#26343F;
    margin:2pt 0 2pt 18pt; padding:3pt 6pt;
    border-radius:3pt; white-space:pre-wrap; word-break:break-all;
}
ul { margin:2pt 0 2pt 26pt; padding:0; }
li { margin:1pt 0; font-size:9.5pt; }
.tip {
    background:#E2EFDA; border-left:3pt solid #378610;
    padding:3pt 7pt; margin:3pt 0 3pt 8pt; font-size:8.5pt;
}
.tip strong { color:#378610; }
.trap {
    background:#FCE4D6; border-left:3pt solid #C00000;
    padding:3pt 7pt; margin:3pt 0 3pt 8pt; font-size:8.5pt;
}
.trap strong { color:#C00000; }
.complexity-table {
    width:100%; border-collapse:collapse; font-size:8.5pt;
    margin:4pt 0 4pt 8pt;
}
.complexity-table th {
    background:#1F3964; color:white; padding:3pt 6pt; text-align:center;
}
.complexity-table td {
    border:1pt solid #BFBFBF; padding:2pt 6pt; text-align:center;
}
.complexity-table tr:nth-child(even) td { background:#F2F2F2; }
"""

# ── CONTENT ─────────────────────────────────────────────────────
body = []

# ── COVER ───────────────────────────────────────────────────────
body.append(f"""
<div class="cover">
  <h1>Data Structures &amp; Algorithms</h1>
  <p class="subtitle">Highlighted Study Summary &ndash; 60 Key Items</p>
  <br>
  <p class="course">Chapters 1&ndash;10 Complete Coverage</p>
  <br>
  <div class="legend">
    <span class="badge-green">GREEN</span> 33 highlights &nbsp;&nbsp;
    <span class="badge-yellow">YELLOW</span> 6 highlights &nbsp;&nbsp;
    <span class="badge-red">RED</span> 4 highlights &nbsp;&nbsp;
    = 43 highlighted + 20 additional
  </div>
  <br>
  <p style="font-size:9pt; color:#444;">
    Part 1: Highlighted items from PDFs (Chapters 1–10)<br>
    Part 2: 20 Additional essential definitions
  </p>
  <br><br>
  <p class="date-line">Prepared: {date.today().strftime('%B %Y')}</p>
</div>
""")

# ════════════════════════════════════════════════════════════════
# PART 1 – HIGHLIGHTED ITEMS
# ════════════════════════════════════════════════════════════════
body.append(divider("PART 1 — Highlighted Items from PDFs (43 items)"))

# ── CHAPTER 1 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 1: Introduction to Python &amp; Data Structures"))
body.append(section("Yellow Highlights — Foundational Concepts"))

body.append(term("Data",
    "A collection of facts and figures; a set of values in a particular format "
    "referring to a single set of item values. Can be stored in different forms such as text, numbers, and images.",
    "yellow"))

body.append(term("Data Structure (Linear vs Non-linear)",
    "A linear data structure has elements that combine to form a specific order "
    "(Arrays, Queues, Stacks, Linked Lists). "
    "Non-linear structures represent data with a hierarchical relationship (Trees, Graphs).",
    "yellow"))

body.append(term("Algorithm",
    "A finite set of logic or instructions for solving a computational problem; "
    "data structures and algorithms are two core elements of every large and complex software project.",
    "yellow"))

body.append(term("if...else / elif Statement",
    "Controls conditional execution of statements; format is a series of if and elif "
    "statements followed by a final else statement.",
    "yellow"))

body.append(term("Higher-Order Functions",
    "Functions that take other functions as arguments or return functions as results. "
    "Python 3 built-in examples: filter() and map().",
    "yellow"))

body.append(term("Base Case (Recursion)",
    "To stop a recursive function from turning into an infinite loop, at least one "
    "argument must test for a terminating condition to end the recursion.",
    "yellow"))

body.append(section("Green Highlights — Python Essentials"))

body.append(term("Python Variables (Dynamic Typing)",
    "In Python, it is not required to first declare the datatype for variables. "
    "Variables point to an object that can change type at any time during execution.",
    "green"))

body.append(term("Function",
    "A block of code which only runs when it is called. "
    "A function can receive data as parameters and return data as a result. "
    "Defined using the def keyword in Python.",
    "green"))

body.append(term("Recursion",
    "Occurs when a function makes one or more calls to itself during execution. "
    "Difference from iteration: recursion uses the call stack; iteration uses a loop.",
    "green"))

body.append(term("Inheritance (OOP)",
    "Allows a new class to inherit functionality from other classes. "
    "Inheritance enables code reuse and modification of existing behavior without rewriting.",
    "green"))

body.append(tip("Python uses duck typing — the type is determined at runtime, not compile time. This is called dynamic typing."))
body.append(tip("A recursive function without a base case will cause a RecursionError (stack overflow)."))
body.append(trap("Higher-order functions (map, filter) are not for sorting — use sorted() with key= for sorting. Do not confuse them."))
body.append(trap("Linear data structures are NOT the same as linear time O(n). 'Linear' in DS means sequential ordering of elements."))

# ── CHAPTER 3 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 3: Algorithm Analysis &amp; Big-O Notation"))
body.append(section("Green Highlights"))

body.append(term("Divide and Conquer Paradigm",
    "Involves: (1) breaking a problem into smaller simpler sub-problems, "
    "(2) solving those sub-problems independently, (3) combining their results.",
    "green"))

body.append(term("Big-O Notation",
    "The letter O stands for order, in recognition that growth rates are defined as "
    "the order of a function. Describes the upper bound of time/space complexity.",
    "green"))

body.append(term("Common Complexity Classes (Growth Rates)",
    "From fastest to slowest: O(1) constant, O(log n) logarithmic, O(n) linear, "
    "O(n log n) linearithmic, O(n²) quadratic, O(2ⁿ) exponential.",
    "green"))

body.append("""<table class="complexity-table">
<tr><th>Notation</th><th>Name</th><th>Example</th></tr>
<tr><td>O(1)</td><td>Constant</td><td>Array index lookup</td></tr>
<tr><td>O(log n)</td><td>Logarithmic</td><td>Binary search</td></tr>
<tr><td>O(n)</td><td>Linear</td><td>Linear search</td></tr>
<tr><td>O(n log n)</td><td>Linearithmic</td><td>Merge sort, Quick sort (avg)</td></tr>
<tr><td>O(n²)</td><td>Quadratic</td><td>Bubble sort, Selection sort</td></tr>
<tr><td>O(2ⁿ)</td><td>Exponential</td><td>Recursive Fibonacci</td></tr>
</table>""")

body.append(tip("Big-O always describes the WORST-case or upper bound. Big-Ω (Omega) describes the best case. Big-Θ (Theta) describes the exact bound."))
body.append(trap("O(2n) simplifies to O(n) — constants are always dropped in Big-O notation. Never keep constant coefficients."))

# ── CHAPTER 4 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 4: Linked List Operations"))
body.append(section("Green Highlights"))

body.append(term("Singly Linked List — Time Complexity of Operations",
    "The worst-case running time (time complexity) of a lookup/access by index is O(n). "
    "Insert/delete at the beginning (with pointer) is O(1).",
    "green"))

body.append(term("delete() Method — Linked List",
    "The delete operation to remove a node has the time complexity of O(n) in the worst case "
    "(must traverse the list to find the node). Removing the head node is O(1).",
    "green"))

body.append(tip("For singly linked lists, always track both 'current' and 'previous' pointers when deleting a middle node."))
body.append(trap("Accessing an element by index in a linked list is O(n) — unlike arrays which are O(1). This is a key trade-off."))

# ── CHAPTER 5 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 5: Stacks &amp; Queues"))
body.append(section("Green Highlights"))

body.append(term("peek() Method — Stack",
    "Returns the top element from the stack without deleting it from the stack. "
    "peek just returns the topmost element; pop() returns and removes it.",
    "green"))

body.append(term("Queue — Time Complexity",
    "The time complexity of enqueue and dequeue operations is O(1). "
    "A doubly linked list with FIFO access is the natural implementation of a queue.",
    "green"))

body.append(term("Queue Implementations",
    "Queue can be implemented using: (1) Python list, (2) pointer structures (linked list), "
    "(3) doubly linked list, (4) Python collections.deque.",
    "green"))

body.append(tip("Stack = LIFO (Last In, First Out). Queue = FIFO (First In, First Out). Know both acronyms."))
body.append(tip("Python's collections.deque is the most efficient queue implementation — O(1) for append and popleft."))
body.append(trap("pop() on an empty stack returns None (not an error) in Python implementation — always check for empty stack before popping."))
body.append(trap("A Python list can simulate a stack but is O(n) for insertions at position 0. Use append/pop for O(1) stack operations."))

# ── CHAPTER 6 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 6: Trees &amp; Tree Traversal"))
body.append(section("Green Highlights"))

body.append(term("Binary Tree",
    "A collection of nodes where each node can have zero, one, or two child nodes. "
    "A simple binary tree node has a data attribute plus left_child and right_child pointers.",
    "green"))

body.append(term("Binary Tree Node Creation",
    "To test the binary tree class, four nodes are created: n1 (root), n2 (left child), "
    "n3 (right child), n4 (left grandchild). Linked by assigning n1.left_child = n2, etc.",
    "green"))

body.append(term("Pre-order Traversal (DFS)",
    "Works as follows: (1) Start at the root node, (2) traverse left sub-tree recursively, "
    "(3) traverse right sub-tree recursively. Order: Root → Left → Right.",
    "green"))

body.append(term("Breadth-First Traversal (BFS)",
    "Starts from the root of the tree and visits every node on the next level "
    "before going deeper. Uses a queue internally. Also called level-order traversal.",
    "green"))

body.append(tip("Three DFS orders: Pre-order (Root→L→R), In-order (L→Root→R), Post-order (L→R→Root). In-order on a BST gives sorted output."))
body.append(trap("BFS uses a queue; DFS uses a stack (or recursion). Never confuse which data structure each traversal uses internally."))

# ── CHAPTER 7 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 7: Hash Tables &amp; Hashing"))
body.append(section("Green Highlights"))

body.append(term("Hash Table Implementation",
    "To implement a hash table, start by creating a class to hold hash table items. "
    "Items must have a key and a value. The hash function maps keys to integer indices.",
    "green"))

body.append(tip("A perfect hash function maps every key to a unique index with no collisions. In practice, collisions must be handled."))
body.append(trap("Hash table lookup is O(1) on average but O(n) in the worst case (all keys hash to the same bucket). Never assume always O(1)."))

# ── CHAPTER 8 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 8: Graphs &amp; Graph Algorithms"))
body.append(section("Green Highlights"))

body.append(term("Undirected Graph",
    "A graph where the pairings representing edges are unordered. "
    "Defined as a collection of vertices V = {v1, v2, …, vn} with unordered edge pairs {vi, vj}.",
    "green"))

body.append(term("Undirected Graph — Edge Properties",
    "An edge in an undirected graph can be traversed in either direction. "
    "An undirected graph is complete if it has the maximum number of edges connecting all vertices.",
    "green"))

body.append(term("Directed Graph — Vertex Degree",
    "The degree of a vertex in a directed graph has two components: "
    "out-degree (total edges leaving the vertex) and in-degree (total edges entering the vertex).",
    "green"))

body.append(term("Source and Sink Vertices",
    "Source vertex: a vertex with an in-degree of zero (no incoming edges). "
    "Sink vertex: a vertex with an out-degree of zero (no outgoing edges).",
    "green"))

body.append(term("Graph Implementation — Adjacency Lists",
    "Strategy: use a set of graph nodes where each node contains a linked list "
    "storing the edges within that node. For weighted graphs, each edge stores the weight.",
    "green"))

body.append(term("Graph Implementation — Adjacency Lists (continued)",
    "Uses a set of graph nodes which generate a set of lists. "
    "Can be implemented in different ways depending on whether the graph is directed or undirected.",
    "green"))

body.append(term("Adjacency List Representation",
    "Representing the set of vertices adjacent to each vertex as a list, "
    "thus generating a set of lists — one list per vertex.",
    "green"))

body.append(section("Red Highlights — Graph &amp; Sorting"))

body.append(term("Adjacency List — Vertex List Generation",
    "This involves representing the set of vertices adjacent to each vertex as a list, "
    "thus generating a set of lists.",
    "red"))

body.append(tip("Adjacency matrix is O(V²) space; adjacency list is O(V+E) space. Use adjacency list for sparse graphs."))
body.append(trap("In-degree and out-degree are only defined for directed graphs. An undirected graph only has 'degree'. Do not mix them up."))

# ── CHAPTER 9 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 9: Searching Algorithms"))
body.append(section("Green Highlights"))

body.append(term("Search Algorithm Types",
    "Categorized into two broad types: (1) algorithms applied to a list of items that are "
    "already sorted, (2) algorithms applied to an unordered list.",
    "green"))

body.append(term("Linear Search",
    "Simply examines each item in the search pool, one at a time, until either the target "
    "is found or the entire pool has been exhausted. Time complexity: O(n).",
    "green"))

body.append(term("Binary Search",
    "A search strategy used to find elements within a sorted array or list. "
    "Works by repeatedly halving the search space. Requires the list to be sorted first. "
    "Time complexity: O(log n).",
    "green"))

body.append(tip("Binary search requires the list to be sorted. If the list is unsorted, you must sort first (O(n log n)) then search O(log n)."))
body.append(trap("Linear search works on unsorted data; binary search only works on sorted data. Never apply binary search to an unsorted list."))

# ── CHAPTER 10 Highlights ────────────────────────────────────────
body.append(chapter("Chapter 10: Sorting Algorithms"))
body.append(section("Red Highlights — Chapter Overview"))

body.append(term("Sorting Algorithms Covered",
    "The most important and popular sorting techniques: Bubble sort, Insertion sort, "
    "Selection sort, Quick sort, Heap sort. Comparison of their time complexities is essential.",
    "red"))

body.append(term("Sorting — Definition",
    "Sorting means arranging all items in a list in ascending order of their magnitude. "
    "Different algorithms have different performance characteristics.",
    "red"))

body.append(term("Heap Sort",
    "Uses a binary heap data structure. After removing or adding an element, "
    "heap order property must always be maintained. Time complexity: O(n log n).",
    "red"))

body.append(section("Green Highlights — Algorithm Details"))

body.append(term("Bubble Sort — Mechanism",
    "Given an unordered list, compare adjacent elements and after each comparison "
    "place them in the right order (swap if needed). Largest bubbles to the end each pass.",
    "green"))

body.append(term("Bubble Sort — Implementation",
    "Works in a double-nested loop: the inner loop repeatedly compares adjacent elements "
    "and swaps them. Time complexity: O(n²) worst and average case.",
    "green"))

body.append(term("Insertion Sort — Complexity",
    "Gives a worst-case runtime complexity of O(n²) and a best-case complexity of O(n) "
    "(when the list is already sorted).",
    "green"))

body.append(term("Selection Sort",
    "Begins by finding the smallest element in the list and swapping it with the "
    "first position, then repeats for remaining positions. Time complexity: O(n²) always.",
    "green"))

body.append(term("Quick Sort — Pivot Placement",
    "After the first iteration of the quick sort algorithm, the chosen pivot point is "
    "placed in its correct position in the list. All elements left of pivot are smaller; all right are larger.",
    "green"))

body.append(term("Sorting Complexity Comparison",
    "A comparison of sorting algorithm complexities: Bubble/Insertion/Selection = O(n²) worst. "
    "Merge sort = O(n log n) always. Quick sort = O(n log n) average, O(n²) worst.",
    "green"))

body.append(tip("Merge sort is the most consistent O(n log n) sorting algorithm. Quick sort is faster in practice but has O(n²) worst case."))
body.append(tip("Selection sort makes exactly n-1 swaps regardless of input. Insertion sort is best for nearly-sorted data."))
body.append(trap("Quick sort is NOT always O(n log n) — its worst case is O(n²) when the pivot is always the smallest or largest element."))
body.append(trap("Bubble sort and Selection sort are never efficient for large datasets — both are O(n²). Do not use them in production."))

# ════════════════════════════════════════════════════════════════
# PART 2 – ADDITIONAL 20 DEFINITIONS
# ════════════════════════════════════════════════════════════════
body.append(divider("PART 2 — Additional 20 Essential Definitions"))

body.append(chapter("Linked Lists (Chapter 4)"))
body.append(section("Core Definitions"))

body.append(term("Linked List",
    "A dynamic data structure consisting of a sequence of nodes, where each node "
    "contains data and a pointer/reference to the next node. Size can grow or shrink at runtime."))

body.append(term("Node",
    "The basic building block of a linked list. Each node stores data and a reference "
    "to the next node. The last node's next pointer is None (null)."))

body.append(term("Singly Linked List",
    "A linked list where each node has only one pointer — to the next node. "
    "Traversal is only possible in one direction (forward)."))

body.append(term("Doubly Linked List",
    "A linked list where each node has two pointers: one to the next node and one to "
    "the previous node. Enables traversal in both directions."))

body.append(term("Head Pointer",
    "A reference to the first node in a linked list. If the head is None, "
    "the list is empty. Losing the head pointer means losing access to the entire list."))

body.append(tip("Linked lists have O(1) insertion/deletion at the head but O(n) random access. Arrays have O(1) random access but O(n) insertion."))
body.append(trap("A linked list is NOT an array — it does not support index-based access in O(1). Every access requires traversal from the head."))

body.append(chapter("Stacks &amp; Queues — Core Definitions (Chapter 5)"))

body.append(term("Stack",
    "A LIFO (Last In, First Out) data structure where elements are inserted and removed "
    "from the same end (the top). Primary operations: push and pop."))

body.append(term("Queue",
    "A FIFO (First In, First Out) data structure where elements are inserted at the rear "
    "(enqueue) and removed from the front (dequeue)."))

body.append(term("Push Operation",
    "Adds a new element to the top of the stack. The top pointer advances to the new node. "
    "Time complexity: O(1)."))

body.append(term("Pop Operation",
    "Removes and returns the topmost element of the stack. Returns None if the stack is empty. "
    "Time complexity: O(1)."))

body.append(term("Enqueue / Dequeue",
    "Enqueue adds an element to the rear of the queue. "
    "Dequeue removes an element from the front. Both are O(1) with a doubly linked list."))

body.append(tip("The call stack in programming is literally a stack — function calls are pushed; returns pop them off."))
body.append(trap("Queue insertion is at the rear; removal is from the front. Never insert and remove from the same end (that would be a stack)."))

body.append(chapter("Trees — Core Definitions (Chapter 6)"))

body.append(term("Root Node",
    "The first (topmost) node of a tree from which all other nodes are attached. "
    "Every tree has exactly one unique root node. It has no parent."))

body.append(term("Leaf Node",
    "A node that does not have any children; it is the terminal node of the tree. "
    "The degree of a leaf node is always 0."))

body.append(term("Tree Height",
    "The total number of nodes in the longest path from root to a leaf. "
    "Depth of a node = number of edges from the root to that node."))

body.append(term("Binary Search Tree (BST)",
    "A binary tree where for every node: all values in the left subtree are less than the node, "
    "and all values in the right subtree are greater. Enables O(log n) search."))

body.append(tip("In-order traversal of a BST always produces elements in sorted (ascending) order."))
body.append(trap("A binary tree ≠ a binary search tree. A binary tree just limits 2 children; a BST also enforces the ordering property."))

body.append(chapter("Hashing &amp; Graphs — Core Definitions (Ch. 7–8)"))

body.append(term("Hash Function",
    "A function that maps input data of arbitrary size to a fixed-size integer (the hash value). "
    "Used as an index into the hash table array. Hashing converts strings to integers."))

body.append(term("Hash Collision",
    "Occurs when two different keys produce the same hash value. "
    "Handled using chaining (linked list at each bucket) or open addressing (linear probing)."))

body.append(term("Graph",
    "A non-linear data structure consisting of a set of vertices (nodes) V "
    "and a set of edges E connecting pairs of vertices. Models relationships between objects."))

body.append(term("Directed Graph (Digraph)",
    "A graph where edges have a direction — an edge from v1 to v2 does not imply "
    "an edge from v2 to v1. Each edge is an ordered pair (vi, vj)."))

body.append(tip("Dictionaries in Python are implemented using hash tables — that is why average lookup is O(1)."))
body.append(trap("A graph with V vertices can have at most V(V-1)/2 edges (undirected). Exceeding this is impossible — do not miscalculate."))

# ── BUILD HTML ──────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>{CSS}</style>
</head>
<body>
{''.join(body)}
</body>
</html>"""

with open("ds_summary.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved: ds_summary.html")

from weasyprint import HTML as WHTML
WHTML(string=html).write_pdf("ds_summary.pdf")
print("Saved: ds_summary.pdf")
