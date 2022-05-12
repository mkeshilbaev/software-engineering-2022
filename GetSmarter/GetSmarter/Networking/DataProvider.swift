//
//  DataProvider.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 13.05.2022.
//

import Foundation
import Firebase

class DataProvider {
    var ref: DatabaseReference!
    
    init() {
        ref = Database.database().reference()
    }
    
    func getCourses(completion: (([Course]) -> Void)? = nil) {
        ref.child("courses").getData { (error, snapshot) in
            let count = snapshot.childrenCount
            var courses: [Course] = []
            
            for index in stride(from: 1, through: count, by: 1) {
                let courseSnapshot = snapshot.childSnapshot(forPath: "\(index)")
                let course = Course(snapshot: courseSnapshot)
                
                if let course = course {
                    courses.append(course)
                }
            }
            completion?(courses)
        }
    }
    
    
//    func addToFavorite(course: Course) {
//        ref.child("course").child("\(course.id)").setValue(course.dict)
//    }
    
//    func removeFromFavorite(course: Course) {
//        ref.child("courses").child("\(course.id)").setValue(course.dict)
//    }
    
    func getCategories(completion: (([Category]) -> Void)? = nil) {
        ref.child("categories").getData { (error, snapshot) in
            let count = snapshot.childrenCount
            var categories: [Category] = []
            
            for index in stride(from: 1, through: count, by: 1) {
                let categorySnapshot = snapshot.childSnapshot(forPath: "\(index)")
                let category = Category(snapshot: categorySnapshot)
                
                if let category = category {
                    categories.append(category)
                }
            }
            completion?(categories)
        }
    }
    
    
    
    
}
