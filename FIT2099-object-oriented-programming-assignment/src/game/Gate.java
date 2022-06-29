package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Item;

public class Gate extends Item {
	
	/**
	 * Constructor.
	 * @param name 		  the name of this Item
	 * @param displayChar the character to use to represent this item if it is on the ground
	 */
	public Gate(String name, char displayChar) {
		super(name, displayChar, false);
	}
	
	/**
	 * Adds Action to list of allowable actions for otherActors to perform
	 * @param action the Action to be added
	 */
	public void addAction(Action action) {
		super.allowableActions.add(action);
	}
	
	/**
	 * Accessor for the Item's price when bought from the Shop.
	 * @return the Item's price
	 */
	@Override
	public double getPrice() {
		return 0;
	}
	
	/**
	 * Accessor for the Item's cost when sold to the Shop.
	 * @return the Item's cost
	 */
	@Override
	public double getCost() {
		return 0;
	}
}
