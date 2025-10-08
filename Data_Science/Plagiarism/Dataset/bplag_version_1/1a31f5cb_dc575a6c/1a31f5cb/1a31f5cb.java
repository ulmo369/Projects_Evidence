import java.util.*;
import java.io.*;

public class Solution
{
    static class Reader {
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
            din = new DataInputStream(
                new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public String readLine() throws IOException
        {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    if (cnt != 0) {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
        }
 
        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
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
            } while ((c = read()) >= '0' && c <= '9');
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
            } while ((c = read()) >= '0' && c <= '9');
 
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
 
            if (neg)
                return -ret;
            return ret;
        }
 
        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
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
    
    static void dfs(int n , LinkedList<Integer> g[] , int arr[][] , int p , long dp[][])
    {
        for(Integer i : g[n])
        {
            if(i != p)
            {
                dfs(i,g,arr,n,dp);
            dp[n][0] += Math.max(dp[i][0]+Math.abs(arr[n][0]-arr[i][0]) , 
                       dp[i][1]+Math.abs(arr[n][0]-arr[i][1]));
                       
                 
            dp[n][1] += Math.max(dp[i][0]+Math.abs(arr[n][1]-arr[i][0]) , 
                       dp[i][1]+Math.abs(arr[n][1]-arr[i][1]));
            }                
        }
    }
    public static void main(String []args) throws IOException
    {
        Reader sc = new Reader();
        StringBuffer str = new StringBuffer("");
        int t  = sc.nextInt();
        while(t-- > 0)
        {
            int n = sc.nextInt();
            int arr[][] = new int[n][2];
            for(int i = 0 ; i < n;  i++)
            {
                arr[i][0] = sc.nextInt();
                arr[i][1] = sc.nextInt();
            }
            LinkedList<Integer> g[] = new LinkedList[n];
            for(int i = 0 ; i < n ; i++)
            {
                g[i] = new LinkedList<Integer>();
            }
            for(int i = 0 ; i < n-1 ; i++)
            {
                int x = sc.nextInt()-1;
                int y = sc.nextInt()-1;
                g[x].add(y);
                g[y].add(x);
            }
            long dp[][] = new long[n][2];
            dfs(0,g,arr,-1 , dp);
            str.append(Math.max(dp[0][0] , dp[0][1]));
            str.append(System.lineSeparator());
        }
        System.out.println(str);
    }
}
