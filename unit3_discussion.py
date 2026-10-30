"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # list.insert() places the value at the given index.
    # Every element that was at that index or later is shifted one
    # position to the right to make room for the new value.
    #
    # Performance: insertion cost depends on WHERE it happens.
    # - At the end: nothing has to shift, so it is fast (O(1)).
    # - At the beginning: every existing element must shift, so it is
    #   the slowest case (O(n)).
    # - In the middle: roughly half the elements shift (still O(n)).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Index validation matters because pop() with an index that does not
    # exist raises an IndexError and would crash the program. Checking
    # first lets us handle the problem gracefully instead.
    # (Negative indexes are treated as invalid here to keep behavior simple
    # and predictable.)
    if index < 0 or index >= len(lst):
        return None

    # Safe deletion: pop() removes the item AND returns it, so we can
    # report what was removed. All elements after the removed one shift
    # left by one position to close the gap, so deleting near the front
    # is slower (O(n)) than deleting at the end (O(1)).
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a LINEAR search because a plain list has no ordering or
    # lookup structure we can exploit. The only way to find a value is to
    # check each element one at a time, starting at index 0 and moving
    # forward sequentially until we find a match or reach the end.
    # Best case: found at index 0 (O(1)). Worst case: found last or
    # missing, so every element is checked (O(n)).
    for i, item in enumerate(lst):
        if item == value:
            return i  # Found it, so stop scanning immediately.

    # We scanned the whole list without a match.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Create a list containing several values.
    numbers = [10, 20, 30, 40, 50]

    # Display the original list.
    print(f"Original list: {numbers}")

    # Insert at the beginning (index 0).
    # All five existing elements shift right by one position.
    insert_at(numbers, 0, 5)
    print(f"After inserting 5 at the beginning: {numbers}")

    # Insert in the middle (index 3).
    # Only the elements from index 3 onward shift right.
    insert_at(numbers, 3, 25)
    print(f"After inserting 25 in the middle (index 3): {numbers}")

    # Insert at the end (index = len(list)).
    # Nothing shifts, so this is the cheapest insertion.
    insert_at(numbers, len(numbers), 60)
    print(f"After inserting 60 at the end: {numbers}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print(f"Starting list: {numbers}")

    # Delete from the beginning. The removed value is returned and every
    # remaining element shifts left one position.
    removed = delete_at(numbers, 0)
    print(f"Deleted from beginning: removed {removed}, list is now {numbers}")

    # Delete from the middle. Only the elements after index 3 shift left.
    removed = delete_at(numbers, 3)
    print(f"Deleted from middle (index 3): removed {removed}, list is now {numbers}")

    # Delete from the end. No shifting is needed, so this is the fastest case.
    removed = delete_at(numbers, len(numbers) - 1)
    print(f"Deleted from end: removed {removed}, list is now {numbers}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print(f"Searching in: {numbers}")

    # Search for a value that exists. The function scans left to right
    # and returns the index of the first match.
    result = search_value(numbers, 25)
    print(f"Search for 25: found at index {result}")

    # Search for a value that does not exist. Every element is checked
    # before the function gives up and returns -1.
    result = search_value(numbers, 99)
    print(f"Search for 99: returned {result} (not found, so the whole list was scanned)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Delete using an invalid index.
    # Without validation this would raise an IndexError. Instead we get None.
    result = delete_at(numbers, 100)
    print(f"Delete at invalid index 100: returned {result}, list unchanged: {numbers}")

    # Edge case 2: Insert into an empty list.
    # insert() works on an empty list; the value simply becomes the
    # only element.
    empty = []
    insert_at(empty, 0, "first")
    print(f"Insert into empty list: {empty}")

    # Edge case 3: Delete from an empty list.
    # len(empty) is 0, so every index is invalid and None is returned.
    empty = []
    result = delete_at(empty, 0)
    print(f"Delete from empty list: returned {result}")

    # Edge case 4: Search an empty list.
    # The loop never runs, so we fall straight through to -1.
    result = search_value(empty, 5)
    print(f"Search empty list for 5: returned {result}")

    # ===============================
    # REAL-WORLD SCENARIO: Music Playlist
    # ===============================
    # The README asks for a real-world scenario. A playlist is a list of
    # songs where users add, remove, and look up songs all the time.
    print("\n=== REAL-WORLD SCENARIO: PLAYLIST ===")

    playlist = ["Song A", "Song B", "Song C", "Song D"]
    print(f"Playlist: {playlist}")

    # A listener adds a song to play next (the front of the playlist).
    # With a huge playlist this front insertion would be costly because
    # every song after it shifts down one spot.
    insert_at(playlist, 0, "New Hit")
    print(f"Added 'New Hit' to play next: {playlist}")

    # The listener adds a song to the end of the playlist (cheap).
    insert_at(playlist, len(playlist), "Encore")
    print(f"Added 'Encore' to the end: {playlist}")

    # The listener searches for a song. This is a linear scan, checking
    # each title in order.
    position = search_value(playlist, "Song C")
    print(f"'Song C' is at position {position}")

    # The listener removes that song once it is found.
    removed = delete_at(playlist, position)
    print(f"Removed '{removed}': {playlist}")


if __name__ == "__main__":
    main()