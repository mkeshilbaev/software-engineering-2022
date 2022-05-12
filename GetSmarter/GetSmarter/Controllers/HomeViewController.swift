//
//  HomeViewController.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 13.05.2022.
//

import UIKit
import FirebaseAuth
import FirebaseDatabase

class HomeViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    var current_user: User?
    var courses: [Course] = []
    let dataProvider = DataProvider()
    @IBOutlet weak var my_table_view: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        current_user = Auth.auth().currentUser!
        
        my_table_view.separatorStyle = .none
        
        dataProvider.getCourses { [weak self] (courses) in
            self?.courses = courses
            DispatchQueue.main.async {
                self?.my_table_view.reloadData()
            }
        }
    }
    
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return courses.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "courseCell", for: indexPath) as? HomeViewTableViewCell else { return UITableViewCell() }
        let course = courses[indexPath.row]
        URLSession.shared.dataTask(with: URL(string: course.pictureUrl)!) { (data, response, error) in
            if error != nil {
                return
            }
            if let data = data {
                DispatchQueue.main.async {
                    cell.bookImageView.image = UIImage(data: data)
                }
            }
        }.resume()
        cell.configure(title: course.title, author: course.author)
        return cell
    }
    
//    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
//        let course = courses[indexPath.row]
//        routeToDetails(course: course)
//    }

    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 100
    }
    
    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let translationTransform = CATransform3DTranslate(CATransform3DIdentity, -500, 0, 0)
        cell.layer.transform = translationTransform
        UIView.animate(withDuration: 0.2, delay: 0.2 * Double(indexPath.row), options: .curveEaseOut, animations: {
            cell.layer.transform = CATransform3DIdentity
        })
    }

//    private func routeToDetails(course: Course) {
//        let storyboard = UIStoryboard(name: "Main", bundle: nil)
//        guard let viewController = storyboard.instantiateViewController(identifier: "CourseViewController") as? CourseViewController else { return }
//        viewController.configure(course: course)
//        navigationController?.pushViewController(viewController, animated: true)
//    }
    
    
}
