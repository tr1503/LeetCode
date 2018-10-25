import java.util.Stack;

public class BashBrace {

	public static void main(String[] args) {
		String expr = "a,((a,b)o(m,n)p),b(a,c)";
		System.out.println(bashBrace(expr));
	}

	public static String bashBrace(String expr) {
		Stack<String> stack = new Stack<String>();

		String finalStr = "";

		String str1 = "";
		int index = 0;
		for (int i = 0; i < expr.length();) {
			char ch = expr.charAt(i++);

			if (ch == ',') {
				if (!"".equals(finalStr)) {
					finalStr = finalStr + ",";
				}
				finalStr = finalStr + multiply(str1, expr.substring(index, i - 1));
				str1 = "";
				index = i;
			}

			if (ch == '(') {
				StringBuffer buffer = new StringBuffer();
				i = evaluate(buffer, multiply(str1, expr.substring(index, i - 1)), expr, i);
				str1 = buffer.toString();
				index = i;
			}

		}

		if (!"".equals(finalStr)) {
			finalStr = finalStr + ",";
		}
		finalStr = finalStr + multiply(str1, expr.substring(index, expr.length()));

		return finalStr.replaceAll(",", "\n");
	}

	private static int evaluate(StringBuffer buffer, String str, String expr, int i) {
		int index = i;
		for (; i < expr.length();) {
			char ch = expr.charAt(i++);
			if (ch == ')') {
				buffer.append(multiply(str, expr.substring(index, i - 1)));
				break;
			}
			if (ch == '(') {
				StringBuffer buffer1 = new StringBuffer();
				i = evaluate(buffer1, multiply(str, expr.substring(index, i - 1)), expr, i);
				str = buffer1.toString();
				index = i;
			}

		}
		return i;
	}

	private static String multiply(String str1, String str2) {
		String str1Arr[] = str1.split(",");
		String str2Arr[] = str2.split(",");
		String str = "";
		for (int i = 0; i < str1Arr.length; i++) {
			for (int j = 0; j < str2Arr.length; j++) {
				if (!"".equals(str)) {
					str = str + ",";
				}
				str = str + str1Arr[i] + str2Arr[j];
			}
		}
		return str;
	}
}
