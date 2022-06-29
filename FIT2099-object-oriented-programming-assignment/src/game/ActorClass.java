package game;

import java.util.ArrayList;
import java.util.Collections;
import java.util.EnumMap;
import java.util.List;

import edu.monash.fit2099.engine.Location;

/**
 * An enum class to categorize animals by their diet.
 */
public enum ActorClass {
	HERBIVORE,
	CARNIVORE,
	OMNIVORE,
	LANDBASED, 
	WATERBASED,
	AMPHIBIAN;
	
	private static List<Location> herbivoreFoodSource = new ArrayList<Location>();
	private static List<Location> carnivoreFoodSource = new ArrayList<Location>();
	private static List<Location> omnivoreFoodSource = new ArrayList<Location>();
	private static EnumMap<ActorClass, List<Location>> classToFood = new EnumMap<ActorClass, List<Location>>(ActorClass.class);
	
	static {
		classToFood.put(HERBIVORE, herbivoreFoodSource);
		classToFood.put(CARNIVORE, carnivoreFoodSource);
		classToFood.put(OMNIVORE, omnivoreFoodSource);
	}
	
	/**
	 * Add location of food supply to list of the corresponding animal category.
	 * @param foodLocation location of food supply
	 */
	public void addFoodSource(Location foodLocation) {
		if (!classToFood.get(this).contains(foodLocation)) {
			classToFood.get(this).add(foodLocation);
		}
	}
	
	/**
	 * Removed location of food supply stored in the list of the corresponding animal category once consumed.
	 * @param foodLocation location of food supply
	 */
	public void removeFoodSource(Location foodLocation) {
		if (classToFood.get(this).contains(foodLocation)) {
			classToFood.get(this).remove(foodLocation);
		}
	}
	
	/**
	 * Accessor for the list of locations of food supply of the corresponding animal category.
	 * @return list of locations of food supply
	 */
	public List<Location> getFoodSource() {
		return Collections.unmodifiableList(classToFood.get(this));
	}
}
