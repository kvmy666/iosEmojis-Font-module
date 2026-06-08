"""Create apache-style Word document for DS summary."""
from _keywords import KEYWORDS_RED, KEYWORDS_ORANGE
from docx import Document
from docx.shared import RGBColor, Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import date

BLUE   = RGBColor(0x00, 0x70, 0xC0)
RED    = RGBColor(0xC0, 0x00, 0x00)
GREEN  = RGBColor(0x37, 0x86, 0x10)
NAVY   = RGBColor(0x1F, 0x39, 0x64)
TEAL   = RGBColor(0x17, 0x6B, 0x7F)
BADGE_G = RGBColor(0x70, 0xAD, 0x47)
BADGE_Y = RGBColor(0xFF, 0xB9, 0x00)
BADGE_R = RGBColor(0xFF, 0x4B, 0x6E)
ORANGE = RGBColor(0xC0, 0x55, 0x00)

def set_para_shading(para, fill_hex):
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    pPr.append(shd)

def colorize_run(run, word):
    tok = word.lower().strip(".,;:()")
    if tok in KEYWORDS_RED:
        run.font.color.rgb = RED; run.font.bold = True
    elif tok in KEYWORDS_ORANGE:
        run.font.color.rgb = ORANGE; run.font.bold = True

def add_chapter_heading(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(6)
    para.paragraph_format.space_after  = Pt(2)
    run = para.add_run(text)
    run.font.size = Pt(13); run.font.bold = True; run.font.color.rgb = NAVY
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot = OxmlElement('w:bottom')
    bot.set(qn('w:val'),'single'); bot.set(qn('w:sz'),'6')
    bot.set(qn('w:space'),'1'); bot.set(qn('w:color'),'1F3964')
    pBdr.append(bot); pPr.append(pBdr)

def add_section(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(4)
    para.paragraph_format.space_after  = Pt(1)
    run = para.add_run(text)
    run.font.size = Pt(10.5); run.font.bold = True; run.font.color.rgb = TEAL

def add_divider(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(8)
    para.paragraph_format.space_after  = Pt(4)
    set_para_shading(para, '1F3964')
    run = para.add_run(text)
    run.font.size = Pt(11); run.font.bold = True
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

def add_term(doc, name, definition, badge=None):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(1.5)
    para.paragraph_format.space_after  = Pt(1.5)
    para.paragraph_format.left_indent  = Inches(0.12)

    if badge == "green":
        r = para.add_run("GREEN ")
        r.font.bold = True; r.font.size = Pt(7); r.font.color.rgb = BADGE_G
    elif badge == "yellow":
        r = para.add_run("YELLOW ")
        r.font.bold = True; r.font.size = Pt(7); r.font.color.rgb = BADGE_Y
    elif badge == "red":
        r = para.add_run("RED ")
        r.font.bold = True; r.font.size = Pt(7); r.font.color.rgb = BADGE_R

    r = para.add_run(name + ": ")
    r.font.color.rgb = BLUE; r.font.bold = True; r.font.size = Pt(9.5)

    for word in definition.split():
        run = para.add_run(word + " ")
        run.font.size = Pt(9.5)
        colorize_run(run, word)

def add_tip(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent  = Inches(0.12)
    para.paragraph_format.space_before = Pt(2)
    para.paragraph_format.space_after  = Pt(2)
    set_para_shading(para, 'E2EFDA')
    r = para.add_run("Exam Tip: ")
    r.font.bold = True; r.font.color.rgb = GREEN; r.font.size = Pt(8.5)
    para.add_run(text).font.size = Pt(8.5)

def add_trap(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent  = Inches(0.12)
    para.paragraph_format.space_before = Pt(2)
    para.paragraph_format.space_after  = Pt(2)
    set_para_shading(para, 'FCE4D6')
    r = para.add_run("Exam Trap: ")
    r.font.bold = True; r.font.color.rgb = RED; r.font.size = Pt(8.5)
    para.add_run(text).font.size = Pt(8.5)

def add_code(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent  = Inches(0.2)
    para.paragraph_format.space_before = Pt(1)
    para.paragraph_format.space_after  = Pt(1)
    set_para_shading(para, 'F2F2F2')
    run = para.add_run(text)
    run.font.name = "Courier New"; run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x26, 0x34, 0x3F)


# ── Build Document ───────────────────────────────────────────────
doc = Document()
for section in doc.sections:
    section.top_margin    = Cm(1.6)
    section.bottom_margin = Cm(1.6)
    section.left_margin   = Cm(1.9)
    section.right_margin  = Cm(1.9)
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(9.5)

# Cover
doc.add_paragraph()
doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Data Structures & Algorithms")
r.font.size = Pt(24); r.font.bold = True; r.font.color.rgb = NAVY

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Highlighted Study Summary – 60 Key Items")
r.font.size = Pt(14); r.font.color.rgb = TEAL

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Chapters 1–10 Complete Coverage")
r.font.size = Pt(12); r.font.bold = True

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("GREEN: 33  |  YELLOW: 6  |  RED: 4 + 8 stamps (Ch.2)  →  51 highlighted + 20 additional")
r.font.size = Pt(10)

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(f"Prepared: {date.today().strftime('%B %Y')}")
r.font.size = Pt(10); r.font.color.rgb = RGBColor(0x70,0x70,0x70)
doc.add_page_break()

# PART 1
add_divider(doc, "PART 1 — Highlighted Items from PDFs (43 items)")

# Ch1
add_chapter_heading(doc, "Chapter 1: Introduction to Python & Data Structures")
add_section(doc, "Yellow Highlights — Foundational Concepts")
add_term(doc, "Data", "A collection of facts and figures; a set of values in a particular format referring to a single set of item values.", "yellow")
add_term(doc, "Data Structure (Linear vs Non-linear)", "Linear structures form a specific order (Arrays, Queues, Stacks, Linked Lists). Non-linear structures represent hierarchical relationships (Trees, Graphs).", "yellow")
add_term(doc, "Algorithm", "A finite set of logic or instructions for solving a problem; data structures and algorithms are two core elements of every large and complex software project.", "yellow")
add_term(doc, "if...else / elif Statement", "Controls conditional execution; a series of if and elif statements followed by a final else statement.", "yellow")
add_term(doc, "Higher-Order Functions", "Functions that take other functions as arguments or return functions. Python 3 built-ins: filter() and map().", "yellow")
add_term(doc, "Base Case (Recursion)", "To stop a recursive function from infinite looping, at least one argument must test for a terminating condition.", "yellow")
add_section(doc, "Green Highlights — Python Essentials")
add_term(doc, "Python Variables (Dynamic Typing)", "Not required to declare datatype first. Variables point to an object that can change type during execution.", "green")
add_term(doc, "Function", "A block of code which only runs when it is called. Can return data as a result. Defined using the def keyword.", "green")
add_term(doc, "Recursion", "Occurs when a function calls itself during execution. Must always have a base case to prevent infinite recursion.", "green")
add_term(doc, "Inheritance (OOP)", "Allows a new class to inherit and modify functionality from other classes, enabling code reuse.", "green")
add_tip(doc, "Python uses dynamic typing — type is determined at runtime. A recursive function without a base case causes RecursionError.")
add_trap(doc, "map() and filter() are NOT sorting functions. Use sorted() with key= for sorting. Linear in DS means sequential order, NOT O(n) time.")

# Ch2
add_chapter_heading(doc, "Chapter 2: Python Data Types & Structures")
add_section(doc, "Red Stamp Marks — Method Tables (Pages 10, 11, 15, 16, 18, 19, 21, 25)")
add_term(doc, "Sequence Types — Common Methods (pp. 10–11)",
    "len(s) count; min/max/sum; all(s) True if all elements True; any(s) True if any item True. "
    "s+r concatenates; s*n copies; s[i] indexing; s[i:j:stride] slicing; x in s membership.", "red")
add_term(doc, "Dictionary Methods (p. 15)",
    "d.get(k,v) returns d[k] or v if missing; d.keys() all keys; d.values() all values; "
    "d.items() all key:value pairs; d.pop(k) removes and returns k; d.update(b) merges b into d.", "red")
add_term(doc, "Dictionary Key Rule (p. 16)",
    "Keys must be unique and immutable. d.setdefault(k,v) returns d[k] if found; "
    "if not found, sets d[k]=v and returns v.", "red")
add_term(doc, "Set Methods — Immutable (p. 18)",
    "a.difference(t) elements in a not in t; a.intersection(t) elements in both; "
    "a.union(t) elements in either; a.issubset(t) True if all a in t; a.issuperset(t) True if all t in a.", "red")
add_term(doc, "Mutable Set Methods (p. 19)",
    "s.add(item) adds (nothing if already present); s.discard(item) removes safely; "
    "s.remove(item) removes (raises KeyError if missing); s.pop() removes arbitrary item.", "red")
add_term(doc, "frozenset — Immutable Set (p. 21)",
    "Use frozenset instead of set when you want to use a set as a dict key or add it inside another set. "
    "s.add(s2) raises TypeError; s.add(frozenset(s2)) works.", "red")
add_term(doc, "Array vs List — Memory (p. 25)",
    "array.array stores typed data and uses ~91% less memory than a Python list for large numeric data. "
    "Use arrays when memory efficiency is critical.", "red")
add_tip(doc, "d.get(key, default) never raises KeyError — always safer than d[key] when key may not exist.")
add_tip(doc, "frozenset is hashable and can be used as a dict key or inside another set. Regular set cannot.")
add_trap(doc, "s.remove(item) raises KeyError if item not found. Use s.discard(item) — it never raises an error.")
add_trap(doc, "array.array is NOT a Python list — it only stores one type of element but uses far less memory.")

# Ch3
add_chapter_heading(doc, "Chapter 3: Algorithm Analysis & Big-O Notation")
add_section(doc, "Green Highlights")
add_term(doc, "Divide and Conquer", "Involves: (1) breaking a problem into smaller sub-problems, (2) solving them independently, (3) combining results.", "green")
add_term(doc, "Big-O Notation", "O stands for 'order'. Describes the upper bound of time/space complexity as input size grows.", "green")
add_term(doc, "Complexity Classes", "O(1) constant → O(log n) logarithmic → O(n) linear → O(n log n) linearithmic → O(n²) quadratic → O(2ⁿ) exponential.", "green")
add_tip(doc, "Big-O = worst case upper bound. Big-Ω = best case. Big-Θ = tight/exact bound.")
add_trap(doc, "Constants are always dropped in Big-O: O(2n) = O(n), O(5n²) = O(n²). Never keep constant coefficients.")

# Ch4
add_chapter_heading(doc, "Chapter 4: Linked List Operations")
add_section(doc, "Green Highlights")
add_term(doc, "Singly Linked List — Complexity", "Worst-case lookup by index: O(n). Insert/delete at the beginning (with head pointer): O(1).", "green")
add_term(doc, "delete() Method", "The delete operation to remove a middle node is O(n) worst case; removing the head node is O(1).", "green")
add_tip(doc, "When deleting a middle node in a singly linked list, always track both current and previous node pointers.")
add_trap(doc, "Linked list index access is O(n), NOT O(1). Arrays are O(1) for index access — this is a key trade-off.")

# Ch5
add_chapter_heading(doc, "Chapter 5: Stacks & Queues")
add_section(doc, "Green Highlights")
add_term(doc, "peek() Method", "Returns the top element from the stack without deleting it. pop() returns and removes the element.", "green")
add_term(doc, "Queue — Time Complexity", "Enqueue and dequeue operations are O(1). A doubly linked list with FIFO access is the natural queue implementation.", "green")
add_term(doc, "Queue Implementations", "Can be implemented using: (1) Python list, (2) pointer structures, (3) doubly linked list, (4) collections.deque.", "green")
add_tip(doc, "Stack = LIFO. Queue = FIFO. Python collections.deque gives O(1) append and popleft — most efficient queue.")
add_trap(doc, "pop() on an empty stack returns None — always check for empty stack. Python list insert(0,...) for queue is O(n), not O(1).")

# Ch6
add_chapter_heading(doc, "Chapter 6: Trees & Tree Traversal")
add_section(doc, "Green Highlights")
add_term(doc, "Binary Tree", "Collection of nodes where each node can have zero, one, or two child nodes. Has data, left_child, and right_child attributes.", "green")
add_term(doc, "Binary Tree Node Creation", "Create root n1, left child n2, right child n3, left grandchild n4. Link via n1.left_child = n2, etc.", "green")
add_term(doc, "Pre-order Traversal (DFS)", "Visit order: Root → Left subtree → Right subtree. Traversal starts at root, goes deeper first.", "green")
add_term(doc, "Breadth-First Traversal (BFS)", "Starts at root, visits every node level by level. Uses a queue internally. Also called level-order traversal.", "green")
add_tip(doc, "In-order traversal on a BST produces sorted output. Pre-order: Root→L→R. In-order: L→Root→R. Post-order: L→R→Root.")
add_trap(doc, "BFS uses a queue internally; DFS uses a stack (or recursion). Never confuse which data structure each uses.")

# Ch7
add_chapter_heading(doc, "Chapter 7: Hash Tables")
add_section(doc, "Green Highlights")
add_term(doc, "Hash Table Implementation", "Start by creating a class to hold items with a key and value. The hash function maps keys to integer indices.", "green")
add_tip(doc, "A perfect hash function maps every key to a unique index. In practice, collisions must be handled with chaining or open addressing.")
add_trap(doc, "Hash table lookup is O(1) average but O(n) worst case. Never assume it is always O(1) — depends on collision frequency.")

# Ch8
add_chapter_heading(doc, "Chapter 8: Graphs")
add_section(doc, "Green Highlights")
add_term(doc, "Undirected Graph", "Edges are unordered pairs. Defined as V = {v1,...,vn} vertices with unordered edge pairs {vi, vj}.", "green")
add_term(doc, "Undirected Edge Properties", "Can be traversed in either direction. A graph is complete if it has the maximum number of edges.", "green")
add_term(doc, "Directed Graph — Degree", "Out-degree: edges leaving a vertex. In-degree: edges entering a vertex.", "green")
add_term(doc, "Source and Sink Vertices", "Source vertex: in-degree = 0 (no incoming edges). Sink vertex: out-degree = 0 (no outgoing edges).", "green")
add_term(doc, "Adjacency List Strategy", "Each graph node contains a linked list of its edges. For weighted graphs, each edge also stores its weight.", "green")
add_term(doc, "Adjacency List (continued)", "Generates a set of lists — one per vertex. Can be implemented in different ways depending on graph type.", "green")
add_section(doc, "Red Highlights")
add_term(doc, "Adjacency List — Vertex List", "Representing vertices adjacent to each vertex as a list, thus generating a set of lists.", "red")
add_tip(doc, "Adjacency matrix: O(V²) space. Adjacency list: O(V+E) space. Use adjacency list for sparse graphs.")
add_trap(doc, "In-degree and out-degree are only defined for DIRECTED graphs. Undirected graphs only have 'degree'.")

# Ch9
add_chapter_heading(doc, "Chapter 9: Searching Algorithms")
add_section(doc, "Green Highlights")
add_term(doc, "Search Algorithm Types", "Two types: (1) for sorted lists, (2) for unsorted lists.", "green")
add_term(doc, "Linear Search", "Examines each item one at a time until the target is found or pool is exhausted. Time complexity: O(n).", "green")
add_term(doc, "Binary Search", "Used on sorted arrays/lists. Repeatedly halves the search space. Requires sorted input. Time complexity: O(log n).", "green")
add_tip(doc, "Binary search requires the list to be sorted. Sort first O(n log n), then search O(log n).")
add_trap(doc, "Never apply binary search to an unsorted list — results are unpredictable. Only linear search works on unsorted data.")

# Ch10
add_chapter_heading(doc, "Chapter 10: Sorting Algorithms")
add_section(doc, "Red Highlights — Overview")
add_term(doc, "Sorting Algorithms Covered", "Bubble, Insertion, Selection, Quick, Heap sort — know time complexities of all.", "red")
add_term(doc, "Sorting Definition", "Arranging all items in a list in ascending order of magnitude. Each algorithm has different performance.", "red")
add_term(doc, "Heap Sort", "Uses binary heap structure. Always maintains heap order property. Time complexity: O(n log n).", "red")
add_section(doc, "Green Highlights — Algorithm Details")
add_term(doc, "Bubble Sort", "Compares adjacent elements and swaps them repeatedly. Double-nested loop. Time: O(n²) worst/average.", "green")
add_term(doc, "Bubble Sort — Implementation", "Double-nested loop: inner loop compares adjacent pairs and swaps. Outer loop repeats n-1 times.", "green")
add_term(doc, "Insertion Sort", "Worst case: O(n²). Best case: O(n) when the list is already sorted.", "green")
add_term(doc, "Selection Sort", "Finds the smallest element each pass and swaps it to the correct position. Time: O(n²) always.", "green")
add_term(doc, "Quick Sort", "After first iteration, pivot is placed in its correct position. Left elements < pivot; right elements > pivot.", "green")
add_term(doc, "Sorting Complexity Comparison", "Bubble/Insertion/Selection = O(n²) worst. Merge sort = O(n log n) always. Quick = O(n log n) avg, O(n²) worst.", "green")
add_tip(doc, "Merge sort is the most consistent O(n log n). Quick sort is faster in practice but O(n²) worst case. Selection sort makes exactly n-1 swaps.")
add_trap(doc, "Quick sort is NOT always O(n log n) — worst case is O(n²) with a bad pivot choice (always min or max element).")

# PART 2
add_divider(doc, "PART 2 — Additional 20 Essential Definitions")

add_chapter_heading(doc, "Linked Lists — Core Definitions (Chapter 4)")
add_term(doc, "Linked List", "A dynamic data structure of nodes where each node stores data and a pointer to the next node. Size grows/shrinks at runtime.")
add_term(doc, "Node", "Basic unit of a linked list: stores data and a reference to the next node. Last node's next = None.")
add_term(doc, "Singly Linked List", "Each node has one pointer (to next node only). Traversal is only possible in one direction (forward).")
add_term(doc, "Doubly Linked List", "Each node has two pointers: next and previous. Enables traversal in both directions.")
add_term(doc, "Head Pointer", "Reference to the first node. If head is None, the list is empty. Losing head means losing the entire list.")
add_tip(doc, "Linked lists: O(1) insert/delete at head, O(n) random access. Arrays: O(1) random access, O(n) insertion.")
add_trap(doc, "Linked list does NOT support O(1) index access. Every access requires traversal from the head — it is always O(n).")

add_chapter_heading(doc, "Stacks & Queues — Core Definitions (Chapter 5)")
add_term(doc, "Stack", "LIFO (Last In, First Out) data structure. Elements inserted and removed from the same end (top). Operations: push, pop.")
add_term(doc, "Queue", "FIFO (First In, First Out). Elements inserted at the rear (enqueue) and removed from the front (dequeue).")
add_term(doc, "Push Operation", "Adds a new element to the top of the stack. Top pointer advances to new node. Time: O(1).")
add_term(doc, "Pop Operation", "Removes and returns the topmost element. Returns None if empty. Time: O(1).")
add_term(doc, "Enqueue / Dequeue", "Enqueue adds to the rear; dequeue removes from the front. Both O(1) with doubly linked list.")
add_tip(doc, "The call stack in programming is literally a stack — function calls are pushed on; returns pop them off.")
add_trap(doc, "Queue: insert at rear, remove from front. If you insert and remove from the same end, that is a stack — not a queue.")

add_chapter_heading(doc, "Trees — Core Definitions (Chapter 6)")
add_term(doc, "Root Node", "The first (topmost) node of a tree. Every tree has exactly one root. It has no parent.")
add_term(doc, "Leaf Node", "A node with no children; terminal node of the tree. Degree of leaf node is always 0.")
add_term(doc, "Tree Height & Depth", "Height: total nodes in the longest root-to-leaf path. Depth of node: number of edges from root to that node.")
add_term(doc, "Binary Search Tree (BST)", "Binary tree where left subtree values < node < right subtree values. Enables O(log n) search.")
add_tip(doc, "In-order traversal of a BST always produces sorted (ascending) output.")
add_trap(doc, "Binary tree ≠ BST. A binary tree just limits 2 children; a BST also enforces the ordering property on values.")

add_chapter_heading(doc, "Hashing & Graphs — Core Definitions (Ch. 7–8)")
add_term(doc, "Hash Function", "Maps input of arbitrary size to a fixed-size integer (hash value), used as an array index. Converts strings to integers.")
add_term(doc, "Hash Collision", "When two different keys produce the same hash value. Handled by chaining (linked list) or open addressing (probing).")
add_term(doc, "Graph", "Non-linear structure of vertices V and edges E connecting pairs. Models relationships between objects.")
add_term(doc, "Directed Graph (Digraph)", "Edges have a direction. Edge (v1→v2) does not imply (v2→v1). Each edge is an ordered pair.")
add_tip(doc, "Python dictionaries are implemented using hash tables — that is why average lookup is O(1).")
add_trap(doc, "A graph with V vertices can have at most V(V-1)/2 edges (undirected). Do not exceed this limit in calculations.")

doc.save("ds_summary.docx")
print("Saved: ds_summary.docx")
