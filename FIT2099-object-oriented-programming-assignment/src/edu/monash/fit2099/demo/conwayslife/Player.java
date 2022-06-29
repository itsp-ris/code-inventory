package edu.monash.fit2099.demo.conwayslife;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Menu;
import game.ActorClass;
import game.ActorSpecies;

/**
 * Class representing the Player.
 */
public class Player extends Actor {

	private Menu menu = new Menu();
	private ActorSpecies species = ActorSpecies.HUMANS;
	private ActorClass actorClass = ActorClass.OMNIVORE;

	/**
	 * Constructor.
	 *
	 * @param name        Name to call the player in the UI
	 * @param displayChar Character to represent the player in the UI
	 * @param hitPoints   Player's starting number of hitpoints
	 */
	public Player(String name, char displayChar, int hitPoints) {
		super(name, displayChar, hitPoints);
	}

	@Override
	public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display) {
		if (lastAction.getNextAction() != null)
			return lastAction.getNextAction();

		actions.add(new SleepAction());
		return menu.showMenu(this, actions, display);
	}

	private class SleepAction extends Action {

		private int sleepTime = 200;

		@Override
		public String execute(Actor actor, GameMap map) {
			sleepTime--;
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
			}
			return actor + " is sleeping.";
		}

		@Override
		public String menuDescription(Actor actor) {
			return "Sleep a while";
		}

		@Override
		public Action getNextAction() {
			if (sleepTime > 0)
				return this;

			return null;
		}
	}

	@Override
	public ActorSpecies getSpecies() {
		return species;
	}

	@Override
	public ActorClass getActorClass() {
		return actorClass;
	}

	@Override
	public ActorClass getActorEco() {
		// TODO Auto-generated method stub
		return null;
	}
}
