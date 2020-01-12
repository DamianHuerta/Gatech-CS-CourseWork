import java.util.NoSuchElementException;

/**
 * Your implementation of an ArrayList.
 *
 * @author Damian Huerta-Ortega
 * @version 1.0
 * @userid dhuertaortega3
 * @GTID 903440034
 *
 * Collaborators: I worked on this assignment alone.
 *
 * Resources: N/A
 */
public class ArrayList<T> {

    /*
     * The initial capacity of the ArrayList.
     *
     * DO NOT MODIFY THIS VARIABLE!
     */
    public static final int INITIAL_CAPACITY = 9;

    /*
     * Do not add new instance variables or modify existing ones.
     */
    private T[] backingArray;
    private int size;

    /**
     * Constructs a new ArrayList.
     *
     * Java does not allow for regular generic array creation, so you will have
     * to cast an Object[] to a T[] to get the generic typing.
     */
    public ArrayList() {
        Object[] arr = new Object[INITIAL_CAPACITY];
        backingArray = (T[]) arr;
        size = 0;
    }

    /**
     * Adds the data to the specified index.
     *
     * This add may require elements to be shifted.
     *
     * If sufficient space is not available in the backing array, resize it to
     * double the current length.
     *
     * Must be amortized O(1) for index size and O(n) for all other cases.
     *
     * @param index the index at which to add the new data
     * @param data  the data to add at the specified index
     * @throws java.lang.IndexOutOfBoundsException if index < 0 or index > size
     * @throws java.lang.IllegalArgumentException  if data is null
     */
    public void addAtIndex(int index, T data) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("This data structure does not allow for negative indexing or indexing "
                    + "above the size of the ArrayList");
        } else if (data == null) {
            throw new IllegalArgumentException("This data structure does not allow data elements to be null");
        } else if (size == backingArray.length) {
            resize();
        }
        if (index == 0) {
            addToFront(data);
        } else if (index == size) {
            addToBack(data);
        } else {
            for (int i = size; i > index; i--) {
                backingArray[i] = backingArray[i - 1];
            }
            backingArray[index] = data;
            size++;
        }
    }

    /**
     * Adds the data to the front of the list.
     *
     * This add may require elements to be shifted.
     *
     * Must be O(n).
     *
     * @param data the data to add to the front of the list
     * @throws java.lang.IllegalArgumentException if data is null
     */
    public void addToFront(T data) {
        if (data == null) {
            throw new IllegalArgumentException("This data structure doesn't allow you to add data that is null");
        } else {
            if (size == backingArray.length) {
                resize();
            }
            for (int i = size; i > 0; i--) {
                backingArray[i] = backingArray[i - 1];
            }
            backingArray[0] = data;
            size++;
        }
    }

    /**
     * Adds the data to the back of the list.
     *
     * Must be amortized O(1).
     *
     * @param data the data to add to the back of the list
     * @throws java.lang.IllegalArgumentException if data is null
     */
    public void addToBack(T data) {
        if (data == null) {
            throw new IllegalArgumentException("This data structure does not allow you to add data that is null");
        } else {
            if (size == backingArray.length) {
                resize();
            }
            backingArray[size] = data;
            size++;
        }
    }

    /**
     * Removes and returns the data at the specified index.
     *
     * Do not shrink the backing array.
     *
     * This remove may require elements to be shifted.
     *
     * Must be O(1) for index size - 1 and O(n) for all other cases.
     *
     * @param index the index of the data to remove
     * @return the data formerly located at the specified index
     * @throws java.lang.IndexOutOfBoundsException if index < 0 or index >= size
     */
    public T removeAtIndex(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("You can't use a negative index or a index >= the size");
        } else if (index == size - 1) {
            return removeFromBack();
        } else if (index == 0) {
            return removeFromFront();
        } else {
            T ret = backingArray[index];
            for (int i = index; i < size - 1; i++) {
                backingArray[i] = backingArray[i + 1];
            }
            backingArray[size - 1] = null;
            size--;
            return ret;

        }

    }

    /**
     * Removes and returns the first data of the list.
     *
     * Do not shrink the backing array.
     *
     * This remove may require elements to be shifted.
     *
     * Must be O(n).
     *
     * @return the data formerly located at the front of the list
     * @throws java.util.NoSuchElementException if the list is empty
     */
    public T removeFromFront() {
        if (isEmpty()) {
            throw new NoSuchElementException("The array list is Empty");
        }
        T front = backingArray[0];
        for (int i = 1; i <= size; i++) {
            backingArray[i - 1] = backingArray[i];
            backingArray[i] = null;
        }
        size--;
        return front;
    }

    /**
     * Removes and returns the last data of the list.
     *
     * Do not shrink the backing array.
     *
     * Must be O(1).
     *
     * @return the data formerly located at the back of the list
     * @throws java.util.NoSuchElementException if the list is empty
     */
    public T removeFromBack() {
        if (isEmpty()) {
            throw new NoSuchElementException("You can't remove from an empty list!");
        }
        T back = backingArray[size - 1];
        backingArray[size - 1] = null;
        size--;
        return back;

    }

    /**
     * Returns the data at the specified index.
     *
     * Must be O(1).
     *
     * @param index the index of the data to get
     * @return the data stored at the index in the list
     * @throws java.lang.IndexOutOfBoundsException if index < 0 or index >= size
     */
    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("You can't get an element from a negative index or an index greater "
                    + "than the size");
        } else {
            return backingArray[index];
        }
    }

    /**
     * Returns whether or not the list is empty.
     *
     * Must be O(1).
     *
     * @return true if empty, false otherwise
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Clears the list.
     *
     * Resets the backing array to a new array of the initial capacity and
     * resets the size.
     *
     * Must be O(1).
     */
    public void clear() {
        Object[] arr = new Object[INITIAL_CAPACITY];
        backingArray = (T[]) arr;
        size = 0;
    }

    /**
     * Returns the backing array of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the backing array of the list
     */
    public T[] getBackingArray() {
        // DO NOT MODIFY THIS METHOD!
        return backingArray;
    }

    /**
     * Returns the size of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the size of the list
     */
    public int size() {
        // DO NOT MODIFY THIS METHOD!
        return size;
    }

    /**
     * This is a helper method that resizes the backing array to twice of its current length
     */
    public void resize() {
        Object[] resize = new Object[backingArray.length * 2];
        T[] casted = (T[]) resize;
        for (int i = 0; i < backingArray.length; i++) {
            casted[i] = backingArray[i];
        }
        backingArray = casted;

    }
}

