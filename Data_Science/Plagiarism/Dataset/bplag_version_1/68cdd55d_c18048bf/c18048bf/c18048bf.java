import java.io.*;
import java.util.*;

public class Main {
    static PrintWriter out;
    static Kioken sc;

    public static void main(String[] args) throws FileNotFoundException {
        boolean t = true;
        boolean f = false;
        if (f) {
            out = new PrintWriter("output.txt");
            sc = new Kioken("input.txt");
        } else {
            out = new PrintWriter((System.out));
            sc = new Kioken();
        }

        int tt = 1;
        tt = sc.nextInt();
        while (tt-- > 0) {
            solve();
        }
        out.flush();
        out.close();
    }
 
    static boolean flag = false;
    static List<int[]>[] ans;
    public static void dfs(int index, boolean[] visited, int parent, int val, List<Integer>[] ll){
        if(visited[index]){
            return;
        }

        List<Integer> l1 = ll[index];
        // out.println(" == " + l1 + " " + index);
        if(l1.size() > 2){
            flag = true;
            return;
        }

        visited[index] = true;

        for(int k: l1){
            if(visited[k] == false){
                // out.println(visited[k] + " " + index + " " + k + " " + val);
                ans[index].add(new int[]{k, val});
                ans[k].add(new int[]{index, val});
                dfs(k, visited, index, (val == 2) ? 5 : 2, ll);
            }
        }
    }
    public static void solve() {
        int n = sc.nextInt();
        List<Integer>[] ll = new List[n + 1];

        // out.println(" mm " + n);
        for (int i = 0; i <= n; i++) {
            ll[i] = new ArrayList<>();  
        }
        int[][] store = new int[n][2];
        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            store[i][0] = u;
            store[i][1] = v;
            // out.println(" === " + u + " " + v);
            int mm = Math.min(u, v);
            int mx = Math.max(u, v);
            // out.println(" u " + v + " " + u);
            ll[mm].add(mx);
            ll[mx].add(mm);
            // ll[v].add(u)
        }

        int two = 2;
        int prime = 5;
        flag = false;
        ans = new List[n+1];
        
        int[] arr = new int[n + 1];


        for(int i = 0; i <= n; i++){
            ans[i] = new ArrayList<>();
        }
    
        boolean[] visited = new boolean[n+1];
        List<Integer> one = ll[1];
        if(one.size() > 2){
            out.println(-1);
            return;
        }

        // out.println(" -- " + one);
        visited[1] = true;
        for(int i = 0; i < one.size(); i++){
            if(i == 0){
                ans[1].add(new int[]{one.get(i), 2});
                ans[one.get(i)].add(new int[]{1, 2});
                dfs(one.get(i), visited, -1, 5, ll);
            }else{
                ans[1].add(new int[]{one.get(i), 5});
                ans[one.get(i)].add(new int[]{1, 5});
                dfs(one.get(i), visited, -1, 2, ll);
            }
        }
        if (flag) {
            out.println(-1);
            return;
        }

       for(int i = 0; i < n-1; i++){
        //    out.println(" -- ");
         int u = store[i][0];
         int v = store[i][1];

        //  out.println(" uu " + u + " " + v);
         if(u == 0 || v == 0){
             continue;
         }
         int mm = Math.min(u, v);
         int mx = Math.max(u, v);
         List<int[]> vv = ans[mm];
        //  for(int[] ii:vv){
        //      out.println(Arrays.toString(ii));
        //  }
         if(vv == null){
             continue;
         }
         for(int[] j: vv){
             if(j[0] == mx){
                 out.print(j[1]+ " ");
                 break;
             }
         }
       }
        out.println();
    }

    public static long gcd(long a, long b) {
        while (b != 0) {
            long rem = a % b;
            a = b;
            b = rem;
        }
        return a;
    }

    public static long leftShift(long a) {
        return (long) Math.pow(2, a);
    }

    public static void reverse(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        for (int i = 0; i < arr.length / 2; i++) {
            int temp = arr[i];
            arr[i] = arr[n - 1 - i];
            arr[n - 1 - i] = temp;
        }
        return;
    }

    public static int lower_bound(ArrayList<Integer> ar, int k) {
        int s = 0, e = ar.size();
        while (s != e) {
            int mid = s + e >> 1;
            if (ar.get(mid) <= k) {
                s = mid + 1;
            } else {
                e = mid;
            }
        }
        return Math.abs(s) - 1;
    }

    public static int upper_bound(ArrayList<Integer> ar, int k) {
        int s = 0;
        int e = ar.size();
        while (s != e) {
            int mid = s + e >> 1;
            if (ar.get(mid) < k) {
                s = mid + 1;
            } else {
                e = mid;
            }
        }
        if (s == ar.size()) {
            return -1;
        }
        return s;
    }

    static class Kioken {
        // FileInputStream br = new FileInputStream("input.txt");

        BufferedReader br;
        StringTokenizer st;

        Kioken(String filename) {
            try {
                FileReader fr = new FileReader(filename);
                br = new BufferedReader(fr);
                st = new StringTokenizer("");

            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
            }
        }

        Kioken() {
            try {
                br = new BufferedReader(new InputStreamReader(System.in));
                st = new StringTokenizer("");

            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
            }
        }

        public String next() {
            while (!st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public String nextLine() {
            try {
                return br.readLine();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }

        public boolean hasNext() {
            String next = null;
            try {
                next = br.readLine();
            } catch (Exception e) {
            }
            if (next == null || next.length() == 0) {
                return false;
            }
            st = new StringTokenizer(next);
            return true;
        }
    }
}