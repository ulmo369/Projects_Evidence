import java.util.*;
import java.io.*;

public class code{

	static class Reader
    {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException
        {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String readLine() throws IOException
        {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1)
            {
                if (c == '\n')
                    break;
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
        }

        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do
            {
                ret = ret * 10 + c - '0';
            }  while ((c = read()) >= '0' && c <= '9');

            if (neg)
                return -ret;
            return ret;
        }

        public long nextLong() throws IOException
        {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }

        public double nextDouble() throws IOException
        {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();

            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');

            if (c == '.')
            {
                while ((c = read()) >= '0' && c <= '9')
                {
                    ret += (c - '0') / (div *= 10);
                }
            }

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }

        public void close() throws IOException
        {
            if (din == null)
                return;
            din.close();
        }
    }

	public static int GCD(int a, int b)
    {
      if (b == 0)
        return a;
      return GCD(b, a % b);
    }

	public static void main(String[] arg) throws IOException{
		//Reader in=new Reader();
		Scanner in=new Scanner(System.in);

   int n=in.nextInt();
	 int[] arr=new int[n];
	 ArrayList<Integer> zero=new ArrayList<Integer>();
	 ArrayList<Integer> one=new ArrayList<Integer>();

	 for(int i=0;i<n;i++){
		 arr[i]=in.nextInt();
		 if(arr[i]==0) zero.add(i);
		 else one.add(i);
	 }
   if(one.size()==0) {
		 System.out.println(0);
	 }
	 else{
			 int[][] dp=new int[one.size()][zero.size()];

		   for(int i=0;i<one.size();i++){
				 for(int j=0;j<zero.size();j++){
					 if(i==0 && j==0) dp[i][j]=Math.abs(one.get(i)-zero.get(j));
					 else if(j==0) dp[i][j]=Integer.MAX_VALUE/2;
					 else if(i==0) dp[i][j]=Math.min(dp[i][j-1],Math.abs(one.get(i)-zero.get(j)));
					 else{
						 dp[i][j]=Math.min(dp[i][j-1],dp[i-1][j-1]+Math.abs(one.get(i)-zero.get(j)));
					 }
				 }
			 }

		  System.out.println(dp[one.size()-1][zero.size()-1]);
		}
	}
}
