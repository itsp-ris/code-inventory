package game;

import edu.monash.fit2099.demo.conwayslife.Status;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.engine.Location;
import edu.monash.fit2099.interfaces.FoodInterface;

public class Food extends Item implements FoodInterface {
	private int nutrients;
	private double price;
	private double cost;
	private Status status = Status.STORED;

	public Food(String name, char displayChar, int nutrients, double price, double cost) {
		super(name, displayChar, true);
		this.nutrients = nutrients;
		this.price = price;
		this.cost = cost;
	}
	
	/**
     * Inform a carried Item of the passage of time.
     * 
     * This method is called once per turn, if the Item is being carried.
     * @param currentLocation The location of the actor carrying this Item.
     * @param actor The actor carrying this Item.
     */
	public void tick(Location currentLocation, Actor actor) {
		if (status != Status.STORED) {
			setStatus(Status.STORED);
		}
		
		if (name.contains("Herbivore")) {
			ActorClass.HERBIVORE.removeFoodSource(currentLocation);
		} else {
			ActorClass.CARNIVORE.removeFoodSource(currentLocation);
		}
	}
	
    /**
     * Inform an Item on the ground of the passage of time. 
     * This method is called once per turn, if the item rests upon the ground.
     * @param currentLocation The location of the ground on which we lie.
     */
	public void tick(Location currentLocation) {
		if (status != Status.ONGROUND) {
			setStatus(Status.ONGROUND);
		}
		
		if (name.contains("Herbivore")) {
			ActorClass.HERBIVORE.addFoodSource(currentLocation);
		} else {
			ActorClass.CARNIVORE.addFoodSource(currentLocation);
		}
		
		if (status == Status.EATEN) {
			currentLocation.removeItem(this);
		}
	}
	
	/**
	 * Accessor for the Food's nutrients when consumed.
	 * @return the Food's nutrients
	 */
	@Override
	public int getNutrients() {
		return nutrients;
	}
	
	/**
	 * Accessor for the Food's price when bought from the Shop.
	 * @return the Food's price
	 */
	@Override
	public double getPrice() {
		return price;
	}
	
	/**
	 * Accessor for the Food's cost when sold to the Shop.
	 * @return the Food's cost
	 */
	@Override
	public double getCost() {
		return cost;
	}
	
	/**
	 * Modifies the current condition of the Item.
	 * @param newStatus the status to replace the current status
	 */
	@Override
	public void setStatus(Status newStatus) {
		status = newStatus;
	}
}
