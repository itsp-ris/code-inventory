package game;

import edu.monash.fit2099.demo.conwayslife.Status;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Exit;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.engine.Location;
import edu.monash.fit2099.interfaces.FoodInterface;

public class Egg extends Item implements FoodInterface {
	
	private Actor baby;
	private ActorSpecies species;
	private ActorClass actorClass;
	private ActorClass actorEco;
	private Status status = Status.STORED;
	private int age = 1;

	public Egg(String name, char displayChar, Actor baby) {
		super(name, displayChar, true);
		this.baby = baby;
		species = baby.getSpecies();
		actorClass = baby.getActorClass();
		actorEco = baby.getActorEco();
	}
	
	/**
     * Inform a carried Item of the passage of time.
     * 
     * This method is called once per turn, if the Item is being carried.
     * @param currentLocation The location of the actor carrying this Item.
     * @param actor The actor carrying this Item.
     */
	public void tick(Location currentLocation, Actor actor) {
		age += 1;
	}
	
	/**
     * Inform an Item on the ground of the passage of time. 
     * This method is called once per turn, if the item rests upon the ground.
     * @param currentLocation The location of the ground on which we lie.
     */
	public void tick(Location currentLocation) {
		ActorClass.CARNIVORE.addFoodSource(currentLocation);
		
		if (status == Status.EATEN) {
			currentLocation.removeItem(this);
			ActorClass.CARNIVORE.removeFoodSource(currentLocation);
		} else {
			age += 1;
			if (age >= 20 && hatchEgg(currentLocation)) {
				ActorClass.CARNIVORE.removeFoodSource(currentLocation);
			}
		}
	}
	
	/**
	 * Get exit that is of Dirt instance, if possible
	 * @param currentLocation The location of the ground on which we lie
	 * @return Exit that is of type Dirt or null, if there aren't any
	 */
	private Location getDirtGround(Location currentLocation) {
		for (Exit exit : currentLocation.getExits()) {
			Location adjacent = exit.getDestination();
			
			if (adjacent.getGround() instanceof Dirt && !adjacent.containsAnActor()) {
				return adjacent;
			}
		}
		
		return null;
	}
	
	/**
	 * Get exit that is of Water instance, if possible
	 * @param currentLocation The location of the ground on which we lie
	 * @return Exit that is of type Water or null, if there aren't any
	 */
	private Location getWaterGround(Location currentLocation) {
		for (Exit exit : currentLocation.getExits()) {
			Location adjacent = exit.getDestination();
			
			if (adjacent.getGround() instanceof Water && !adjacent.containsAnActor()) {
				return adjacent;
			}
		}
		
		return null;
	}
	
	/**
	 * Hatch the egg at the suitable adjacent Exit, if possible.
	 * @param currentLocation The location of the ground on which we lie.
	 * @return boolean
	 */
	private boolean hatchEgg(Location currentLocation) {
		Location location;
		
		if (actorEco == ActorClass.LANDBASED) {
			location = getDirtGround(currentLocation);
			
			if (location != null) {
				currentLocation.removeItem(this);
				location.addActor(baby);
				return true;
			}
		} else if (actorEco == ActorClass.WATERBASED) {
			location = getWaterGround(currentLocation);
			
			if (location != null) {
				currentLocation.removeItem(this);
				location.addActor(baby);
				return true;
			}
		} else {
			for (Exit exit : currentLocation.getExits()) {
				location = exit.getDestination();
				if (!location.containsAnActor()) {
					currentLocation.removeItem(this);
					location.addActor(baby);
					return true;
				}
			}
		}
		
		return false;
	}
	
	/**
	 * Accessor for the Egg(s)'s nutrients when consumed.
	 * @return the Egg(s)'s nutrients
	 */
	@Override
	public int getNutrients() {
		return species.getEggNutrients();
	}
	
	/**
	 * Accessor for the Egg(s)'s price when bought from the Shop.
	 * @return the Egg(s)'s price
	 */
	@Override
	public double getPrice() {
		return species.getEggPrice();
	}
	
	/**
	 * Accessor for the Egg(s)'s cost when sold to the Shop.
	 * @return the Egg(s)'s cost
	 */
	@Override
	public double getCost() {
		return species.getEggCost();
	}
	
	/**
	 * Accessor for the age of the Egg
	 * @return the age of the Egg
	 */
	public int getAge() {
		return age;
	}
	
	/**
	 * Accessor for the Actor's (inside the egg) habitat category
	 * @return the Actor's habitat category
	 */
	public ActorClass getActorEco() {
		return actorEco;
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
