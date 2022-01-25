<!-- TOC -->

- [1. Model View View-Model](#1-model-view-view-model)
    - [1.1. Android](#11-android)
    - [1.2. Model View Controller](#12-model-view-controller)
    - [1.3. Model View ViewModel](#13-model-view-viewmodel)
        - [1.3.1. Common Terms](#131-common-terms)
    - [1.4. Activity Life Cycle](#14-activity-life-cycle)

<!-- /TOC -->

# 1. Model View View-Model

## 1.1. Android
* It is an operating system
* Based on BSD 

## 1.2. Model View Controller
* **Model** - the business objects and logic for the applicatioln
* **View** - the visual presentation of information to the user
* **Controller** - taking user inputs and passing data and request to the model

## 1.3. Model View ViewModel
Like MVC, but hte ViewModel primarily deals with data binding between Model and View. 

### 1.3.1. Common Terms
* **Activity** - Visual representation of an android application. Uses both view and fragments to create a user interface. There is normalyy one of these for each screen.
* **Fragment** - Optional construcst inside activities to support display on different devices or provide reuse across multiple activities or to support swiping. 
* **View** - Interface widget like a button or text field. 
* **ViewGroup** - Basically a layout manager to establish where the view will go on the actual screen.
* **Intent** - An async message that allows the application to request functionality from other components.
* **Service** - A background task that does not require a UI component.
* **Content Provider** - An interface to shared application data. Usually the on-board SQLite database.
* **Broadcast Reciever** - Deliver events to the app outside of regular program flow. 

## 1.4. Activity Life Cycle
* Once activity is started, it can be in 3 states: `Paused`, `Resumed/Running` and `Stopped`.
* Have following callbacks to determine what state we are in, `onCreate()`, `onStart()`, `onResume()`, `onPause()`, `onStop()`, `onRestart()` and `onDestroy()`
* Entire lifetime is between create - destory.
* Visible lifetime between start - stop.
* Foreground lifetime between resume - pause.
