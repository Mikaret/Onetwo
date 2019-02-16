//package cs310;
import edu.princeton.cs.algs4.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

/**
 * Class to demonstrate greedy algorithms
 */
public class GridA {
    private boolean[][] grid = null;
    private boolean[][] marked;
    private Queue<Integer> q;
    private List<Set<Spot>> list;
    private Set<Spot> set;

    /**
     * Very simple constructor
     * 
     * @param ingrid
     *            a two-dimensional array of boolean to be used as the grid to
     *            search
     */
    public GridA(boolean[][] ingrid) {
        grid = ingrid;
        marked = new boolean[grid.length][grid[0].length];
        set = new HashSet<Spot>();
        q = new Queue<Integer>();
        list = new LinkedList<>();
        groupsInit();
    }

    public void groupsInit() {
        for (int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if (!marked[i][j]) { findGroups(i, j); }
            }
        }
    }

    /**
     * Main method, creates a Grid, then asks it for the size of the group
     * containing the given point.
     */
    public static void main(String[] args) {
        int i = 0;
        int j = 0;

        // Make sure we've got the right number of arguments
        if (args.length < 2) {
            System.err.println("Incorrect arguments.");
            printUsage();
 			return;
        } else {
            i = Integer.parseInt(args[0]);
            j = Integer.parseInt(args[1]);
        }

        // Usage: java Grid 3 7 to search from (3, 7), top occupied square
        // of L-shaped group of Figure 7.30, pg. 281

        boolean[][] gridData = {
                { false, false, false, false, false, false, false, false,
                        false, true },
                { false, false, false, true, true, false, false, false, false,
                        true },
                { false, false, false, false, false, false, false, false,
                        false, false },
                { false, false, false, false, true, false, false, true, false,
                        false },
                { false, false, false, true, false, false, false, true, false,
                        false },
                { false, false, false, false, false, false, false, true, true,
                        false },
                { false, false, false, false, true, true, false, false, false,
                        false },
                { false, false, false, false, false, false, false, false,
                        false, false },
                { false, false, false, false, false, false, false, false,
                        false, false },
                { false, false, false, false, false, false, false, false,
                        false, false } };

        GridA mygrid = new GridA(gridData);

        int size = mygrid.groupSize(i, j);

        System.out.println("Group size: " + size);
        int groupNo = mygrid.groupCount();
        System.out.println("no. of groups: " + groupNo);
        mygrid.printGroups();
    }

    /**
     * Prints out a usage message
     */
    private static void printUsage() {
        System.out.println("Usage: java Grid <i> <j>");
        System.out
                .println("Find the size of the cluster of spots including position i,j");
    }

    public int groupCount () {
        return list.size();
    }

    public void printGroups() {
        System.out.println("Groups: ");
        for (Set<Spot> c : list) {
            System.out.print(c + " ");
        }
    }

    public int groupSize(int i, int j) {
        for (Set<Spot> s : list) {
            if (s.contains(new Spot(i, j))) { return s.size(); }
        }
        return 0;
    }

    public int findGroups(int i, int j){ //GREEDY
        if (grid[i][j] == false) { return 0; }
        marked[i][j] = true;
        if (!set.contains(new Spot(i, j))) { set.add(new Spot(i, j)); }
        if (i + 1 < grid.length) {
            if (grid[i+1][j] && !marked[i+1][j]) {
                q.enqueue(i+1);
                q.enqueue(j);
                set.add(new Spot(i+1, j));
            }
        }
        if (i - 1 >= 0) {
            if (grid[i-1][j] && !marked[i-1][j]) {
                q.enqueue(i-1);
                q.enqueue(j);
                set.add(new Spot(i-1, j));
            }
        }
        if (j - 1 >= 0) {
            if (grid[i][j-1] && !marked[i][j-1]) {
                q.enqueue(i);
                q.enqueue(j-1);
                set.add(new Spot(i, j-1));
            }
        }
        if (j + 1 < grid[0].length) {
            if (grid[i][j+1] && !marked[i][j+1]) {
                q.enqueue(i);
                q.enqueue(j+1);
                set.add(new Spot(i, j+1));
            }
        }
        if (q.size() == 0) {
            Set<Spot> setCopy = new HashSet<>(set);
            list.add(setCopy);
            set.clear();
            return 1;
        }
        return 1 + findGroups(q.dequeue(), q.dequeue());
    }

    /**
     * Nested class to represent a filled spot in the grid
     */
    private static class Spot {
        int i;
        int j;

        public Spot(int i, int j) {
            this.i = i;
            this.j = j;
        }

        public boolean equals(Object o) {
                if (o == null)
                        return false;
                if (o.getClass() != getClass())
                        return false;
                Spot other = (Spot) o;
                return (other.i == i) && (other.j == j);
        }

        /**
        * Returns an int based on Spot's contents
        * another way: (new Integer(i)).hashCode()^(new Integer(j)).hashCode();
        */
        public int hashCode() {
                return i << 16 + j; // combine i and j two halves of int
        }

        /**
        * Returns a String representing this Spot
        */
        public String toString() {
                return "(" + i + " , " + j + ")";
        }
    }
}

