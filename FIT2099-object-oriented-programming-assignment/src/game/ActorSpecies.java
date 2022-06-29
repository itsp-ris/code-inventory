package game;

import java.util.ArrayList;
import java.util.Collections;
import java.util.EnumMap;
import java.util.List;

import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Location;

/**
 * An enum class to standardize types of Dinosaurs.
 */
public enum ActorSpecies {
	HUMANS,
	PROTOCERATOPS,
	VELOCIRAPTORS,
	FISH,
	PLESIOSAURS,
	PTERANODONS,
	TREX;
	
	//Maps Eggs from each species to its nutrients
	private final static EnumMap<ActorSpecies, Integer> EGGTONUTRIENTS = new EnumMap<ActorSpecies, Integer>(ActorSpecies.class);
	//Maps Eggs from each species to its price when bought from the Shop
	private final static EnumMap<ActorSpecies, Double> EGGTOPRICE = new EnumMap<ActorSpecies, Double>(ActorSpecies.class);
	//Maps Eggs from each species to its cost when sold to the Shop
	private final static EnumMap<ActorSpecies, Double> EGGTOCOST = new EnumMap<ActorSpecies, Double>(ActorSpecies.class);
	
	//Maps Actors to its nutrients
	private final static EnumMap<ActorSpecies, Integer> ACTORTONUTRIENTS = new EnumMap<ActorSpecies, Integer>(ActorSpecies.class);
	//Maps Actors to its cost when sold to the Shop
	private final static EnumMap<ActorSpecies, Double> ACTORTOCOST = new EnumMap<ActorSpecies, Double>(ActorSpecies.class);
	//Maps Actors' corpse to its cost when sold to the Shop
	private final static EnumMap<ActorSpecies, Double> CORPSETOCOST = new EnumMap<ActorSpecies, Double>(ActorSpecies.class);
	
	private static List<Actor> velociraptorsTarget = new ArrayList<Actor>();
	private static List<Actor> plesiosaursTarget = new ArrayList<Actor>();
	private static List<Actor> pteranodonsTarget = new ArrayList<Actor>();
	private static List<Actor> trexTarget = new ArrayList<Actor>();
	private static EnumMap<ActorSpecies, List<Actor>> speciesToTarget = new EnumMap<ActorSpecies, List<Actor>>(ActorSpecies.class);
	
	static {
		EGGTONUTRIENTS.put(PROTOCERATOPS, 10);
		EGGTOPRICE.put(PROTOCERATOPS, (double) 50);
		EGGTOCOST.put(PROTOCERATOPS, (double) 10);
		
		ACTORTONUTRIENTS.put(PROTOCERATOPS, 50);
		ACTORTOCOST.put(PROTOCERATOPS, (double) 100);
		CORPSETOCOST.put(PROTOCERATOPS, (double) 15);
		
		EGGTONUTRIENTS.put(VELOCIRAPTORS, 20);
		EGGTOPRICE.put(VELOCIRAPTORS, (double) 1000);
		
		ACTORTONUTRIENTS.put(VELOCIRAPTORS, 75);
		ACTORTOCOST.put(VELOCIRAPTORS, (double) 2000);
		CORPSETOCOST.put(VELOCIRAPTORS, (double) 300);
		
		ACTORTONUTRIENTS.put(FISH, 20);
		CORPSETOCOST.put(FISH, (double) 0);
		
		EGGTONUTRIENTS.put(PLESIOSAURS, 50);
		EGGTOPRICE.put(PLESIOSAURS, (double) 6000);
		
		ACTORTONUTRIENTS.put(PLESIOSAURS, 100);
		ACTORTOCOST.put(PLESIOSAURS, (double) 20000);
		CORPSETOCOST.put(PLESIOSAURS, (double) 2000);
		
		EGGTONUTRIENTS.put(PTERANODONS, 50);
		EGGTOPRICE.put(PTERANODONS, (double) 6000);
		
		ACTORTONUTRIENTS.put(PTERANODONS, 100);
		ACTORTOCOST.put(PTERANODONS, (double) 20000);
		CORPSETOCOST.put(VELOCIRAPTORS, (double) 2000);
		
		EGGTONUTRIENTS.put(TREX, 150);
		EGGTOPRICE.put(TREX, (double) 60000);
		
		CORPSETOCOST.put(TREX, (double) 40000);
		
		speciesToTarget.put(VELOCIRAPTORS, velociraptorsTarget);
		speciesToTarget.put(PLESIOSAURS, plesiosaursTarget);
		speciesToTarget.put(PTERANODONS, pteranodonsTarget);
		speciesToTarget.put(TREX, trexTarget);
	}
	
	/**
	 * Accessor for the Egg(s)'s nutrients when consumed.
	 * @return the Egg(s)'s nutrients
	 */
	public int getEggNutrients() {
		return EGGTONUTRIENTS.get(this);
	}
	
	/**
	 * Accessor for the Egg(s)'s price when bought from the Shop.
	 * @return the Egg(s)'s price
	 */
	public double getEggPrice() {
		return EGGTOPRICE.get(this);
	}
	
	/**
	 * Accessor for the Egg(s)'s cost when sold to the Shop.
	 * @return the Egg(s)'s cost
	 */
	public double getEggCost() {
		return EGGTOCOST.get(this);
	}
	
	/**
	 * Accessor for the Actor's nutrients when consumed.
	 * @return the Actor's nutrients
	 */
	public int getActorNutrients() {
		return ACTORTONUTRIENTS.get(this);
	}
	
	/**
	 * Accessor for the Actor's cost when sold to the Shop.
	 * @return the Actor's cost
	 */
	public double getActorCost() {
		return ACTORTOCOST.get(this);
	}
	
	/**
	 * Accessor for the Actor's corpse cost when sold to the Shop.
	 * @return the Actor's corpse cost
	 */
	public double getCorpseCost() {
		return CORPSETOCOST.get(this);
	}
	
	/**
	 * Adds target to follow.
	 * @param target the Actor to follow
	 */
	public void addTarget(Actor target) {
		speciesToTarget.get(this).add(target);
	}
	
	/**
	 * Removes target to follow once consumed.
	 * @param target the Actor followed
	 */
	public void removeTarget(Actor target) {
		speciesToTarget.get(this).remove(target);
	}
	
	/**
	 * Accessor for the list of targets to follow.
	 * @return the list of Actors to follow
	 */
	public List<Actor> getTarget() {
		return Collections.unmodifiableList(speciesToTarget.get(this));
	}
}
