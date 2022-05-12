//
//  SearchViewController.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 13.05.2022.
//

import UIKit
import FirebaseAuth


class SearchViewController: UIViewController {
    
    var current_user: User?

    override func viewDidLoad() {
        super.viewDidLoad()
        
        current_user = Auth.auth().currentUser!
    }
    

    @IBAction func logoutPressed(_ sender: UIButton) {
        do{
          try Auth.auth().signOut()
          }catch{
              print("Error while sign out!")
          }
          self.dismiss(animated: true, completion: nil)
    }
}
