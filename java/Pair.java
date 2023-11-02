public class Pair {
    int a;
    int b;

    public Pair(int a, int b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", a, b);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Pair pair = (Pair) o;
        return pair.a == a && pair.b == b;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(a) * 31 + Integer.hashCode(b);
    }
}
