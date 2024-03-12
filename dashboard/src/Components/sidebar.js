import React from 'react';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom
import {
  BsCart3, BsGrid1X2Fill, BsFillArchiveFill, BsListCheck, BsMenuButtonWideFill,
  BsFillGearFill, BsPeopleFill
} from 'react-icons/bs';

function Sidebar({ OpenSidebarToggle, OpenSidebar }) {
  return (
    <aside id="sidebar" className={OpenSidebarToggle ? "sidebar-responsive" : ""}>
      <div className='sidebar-title'>
        <div className='sidebar-brand'>
          FULMINE
        </div>
        <span className='icon close_icon' onClick={OpenSidebar}>X</span>
      </div>

      <ul className='sidebar-list'>
        <li className='sidebar-list-item'>
          <a href="">
            <BsGrid1X2Fill className='icon' /> Dashboard
          </a>
        </li>
        <li className='sidebar-list-item'>
          <a href="">
            <BsFillArchiveFill className='icon' /> Monthly Current Consumption
          </a>
        </li>
        <li className='sidebar-list-item'>
          <a href="">
            <BsListCheck className='icon' /> Production rate
          </a>
        </li>
        <li className='sidebar-list-item'>
          <a href="">
            <BsMenuButtonWideFill className='icon' /> Reports
          </a>
        </li>
      </ul>
      <div className='sidebar-bottom'>
        <ul className='sidebar-list'>
          <li className='sidebar-list-item'>
            {/* Use Link for navigation */}
            <Link to="/settings">
              <BsFillGearFill className='icon' /> Settings
            </Link>
          </li>
          <li className='sidebar-list-item'>
            <a href="">
              <BsPeopleFill className='icon' /> Profile
            </a>
          </li>
        </ul>
      </div>
    </aside>
  )
}

export default Sidebar;
