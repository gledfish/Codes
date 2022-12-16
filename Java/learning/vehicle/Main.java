package learning.vehicle;

class Main{
    public static void main(String[] args) {
        Truck truck1 = new Truck(2, 200, 7, 44000);
        int dist = 252;
        double gallons = truck1.fuelNeeded(dist);
        System.out.println(gallons);
    }
}