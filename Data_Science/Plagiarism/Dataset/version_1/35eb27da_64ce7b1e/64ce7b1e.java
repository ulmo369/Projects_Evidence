import java.io.*;
import java.util.*;
public class new1{
	
    static int gcd(int a, int b)
    {
      if (b == 0)
        return a;
      return gcd(b, a % b);
    }
    

	public static void main(String[] args)  throws IOException{

		BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
		FastReader s = new FastReader();
		int t = s.nextInt();
		for(int z = 0; z < t; z++) {
			int n = s.nextInt();
			Set<String> st = new HashSet<String>();
			String[] arr = new String[n];
			boolean pos = false;
			for(int i = 0; i < n; i++) {
				String str = s.next();
				st.add(str); arr[i] = str;
				if(str.length() == 1) pos = true;
			}
			if(pos) {
				System.out.println("YES");
				continue;
			}
			for(int i = 0; i < n; i++) {
				String str = arr[i];
				st.remove(str);
				if(str.charAt(0) == str.charAt(str.length() - 1)) pos = true;
				if(str.length() == 3) {
					String str1 = Character.toString(str.charAt(1)) + Character.toString(str.charAt(0));
					if(st.contains(str1)) pos = true;
					String str2 = Character.toString(str.charAt(2)) + str1;
					if(st.contains(str2)) pos = true;
				}
				else {
					String str1 = Character.toString(str.charAt(1)) + Character.toString(str.charAt(0));
					if(st.contains(str1)) pos = true;;
					for(int j = 0; j < 26; j++) {
						char ch = (char) ((int)'a' + j);
						String str2 = Character.toString(ch) + str1;
						if(st.contains(str2)) pos = true;;
					}
					
					
				}
			}
			//System.out.println(st.toString());
			if(pos) System.out.println("YES");
			else System.out.println("NO");
			//System.out.println(st.contains("ba"));
		}
			
	  }
}


 
	class FastReader {
	    BufferedReader br;
	    StringTokenizer st;
	    public FastReader() {
	        br = new BufferedReader(new InputStreamReader(System.in));
	    }
	    String next() {
	        while (st == null || !st.hasMoreElements()) {
	            try {
	                st = new StringTokenizer(br.readLine());
	            } catch (IOException e) {
	                e.printStackTrace();
	            }
	        }
	        return st.nextToken();
	    }
	 
	    public int nextInt() {
	        return Integer.parseInt(next());
	    }
	 
	    long nextLong() {
	        return Long.parseLong(next());
	    }
	 
	    double nextDouble() {
	        return Double.parseDouble(next());
	    }
	 
	    String nextLine() {
	        String str = "";
	        try {
	            str = br.readLine();
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	        return str;
	}}