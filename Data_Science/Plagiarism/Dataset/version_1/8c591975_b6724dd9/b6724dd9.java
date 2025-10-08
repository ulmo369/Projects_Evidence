
import java.io.*;
import java.util.*;

public class AirConditioners {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		// System.in and System.out are input and output streams, respectively.
		InputStream inputStream = System.in;

		InputReader in = new InputReader(inputStream);
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = in.nextInt();
		while (t-- != 0) {
			int n = in.nextInt();
			int k = in.nextInt();
			HashMap<Integer, Integer> hm = new HashMap<>();
			int[] ac = in.readArray(k);
			for (int idx = 0; idx < ac.length; idx++) {
				hm.put(ac[idx], in.nextInt());
			}
			Arrays.sort(ac);
			long[] lmin = new long[n];
			long val = (long) Integer.MAX_VALUE;
			int acdx = 0;
			for (int idx = 0; idx < lmin.length; idx++) {
				if (acdx < ac.length && ac[acdx] - 1 == idx) {
					val = (long) Math.min(val, hm.get(ac[acdx]));
					acdx++;
				}
				lmin[idx] = val;
				val++;
			}
			acdx = ac.length - 1;
			val = Integer.MAX_VALUE;
			for (int idx = lmin.length-1; idx >= 0; idx--) {
				if (acdx >= 0 && ac[acdx] - 1 == idx) {
					val = (long) Math.min(val, hm.get(ac[acdx]));
					acdx--;
				}
				lmin[idx] = Math.min(lmin[idx], val);
				val++;
			}
			for (long x : lmin) {
				out.write(x + " ");
			}
			out.newLine();
		}
		out.close();
	}

	static class InputReader {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream), 32768);
			tokenizer = null;
		}

		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
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

		public int[] readArray(int n) {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++)
				arr[i] = nextInt();
			return arr;
		}
	}

}
