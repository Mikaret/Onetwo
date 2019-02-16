
public class Project_1 {

	public static void main(String[] args) {
		Path g = new Path();
		Path n = new Path();
		Path k = new Path();
		
		g.cost =  1;
		n.cost = 2;
		k.cost = 3;
		
		g.next =  n;
		n.next = k;
		k.next = null;
		
	        for (Path p = g; p != null; p = p.next) {
	            System.out.println(p.cost);

		}
	}
	

}
