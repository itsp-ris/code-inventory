package game;

import edu.monash.fit2099.engine.Item;

/**
 * Base class for any item that can be picked up and dropped.
 */
public class PortableDinoItem extends Item {
	private double price;
	private double cost;
	
	/**
	 * Constructor. 
	 * @param name 		  the name of this Item
	 * @param displayChar the character to use to represent this Item if it is on the ground
	 * @param price 	  the price of the Item when bought from the Shop
	 * @param cost 		  the cost of the Item when sold to the Shop
	 */
	public PortableDinoItem(String name, char displayChar, double price, double cost) {
		super(name, displayChar, true);
		this.price = price;
		this.cost = cost;
	}
	
	/**
	 * Accessor for the Item's price when bought from the Shop
	 * @return the price of the Item
	 */
	@Override
	public double getPrice() {
		return price;
	}
	
	/**
	 * Accessor for the Item's cost when sold to the Shop
	 * @return the cost of the Item
	 */
	@Override
	public double getCost() {
		return cost;
	}
}
