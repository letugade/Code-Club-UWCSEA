//
//  ViewController.swift
//  Calculator
//
//  Created by Vaishant Kameswaran on 10/10/17.
//  Copyright © 2017 VaiRox. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {
    var n1 : Double = 0
    var n2 : Double = 0
    var valueStored : Bool = false
    @IBOutlet var btn1: NSButton!
    @IBOutlet var txtDisplay: NSTextField!
    @IBOutlet var btnClear: NSButton!
    @IBOutlet var btnAdd: NSButton!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    @IBAction func pushBtn1(_ sender: NSButton) {
        txtDisplay.stringValue += "1"
    }
    @IBAction func btnAddPushed(_ sender: Any) {
        n1 = Double(txtDisplay.doubleValue)
        txtDisplay.stringValue = ""
        valueStored = true
        btnAdd.isEnabled = false
    }
    @IBAction func btnEqualsPushed(_ sender: Any) {
        n2 = Double(txtDisplay.doubleValue)
        var sum = n1  + n2
        txtDisplay.doubleValue = sum
        valueStored = false
        btnAdd.isEnabled = true
    }
    @IBAction func btnClearPushed(_ sender: Any) {
        txtDisplay.stringValue = ""
        n1 = 0
        n2 = 0
        valueStored = false
        btnAdd.isEnabled = true
    }

}

